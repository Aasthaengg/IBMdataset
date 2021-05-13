N = int(input())
A = list(map(int,input().split()))
a = 0
S = 0
num = 1
for i in range(1,N):
    if A[i] - A[i - 1] == 0:
        a = 0
    elif A[i] - A[i - 1] > 0:
        a = 1
    else:
        a = 2
    if S == 0:
        S = a
    elif (S != a) and (a != 0):
        num += 1
        S = 0
print(num)
