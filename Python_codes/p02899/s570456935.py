N = int(input())
A = list(map(int, input().split()))
a  = []
for i in range(N):
    a.append([A[i], i])
a.sort()
b = []
for i in a:
    b.append(i[-1]+1)
print(*b)