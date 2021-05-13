n = int(input())
A = list(map(int,input().split()))

A.sort()
#print(A)

ans = 0
size = 0
for i in range(n):
    if A[i] <= 2*size:
        ans += 1
    else:
        ans = 1
    size = A[i] + size

print(ans)