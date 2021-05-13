n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
q = int(input())
lst = [0] * q
for i in range(q):
    lst[i] = list(map(int, input().split()))
s = sum(A)
num = [0] * 10**5
for i in A:
    num[i-1] += 1
for i in range(q):
    s += num[lst[i][0]-1] * (lst[i][1] - lst[i][0])
    num[lst[i][1]-1] += num[lst[i][0]-1]
    num[lst[i][0]-1] = 0
    print(s)