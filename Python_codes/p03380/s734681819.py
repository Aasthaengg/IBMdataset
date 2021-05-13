n = int(input())
A = list(map(int, input().split()))
x = max(A)
A.pop(A.index(max(A)))
ans = A[0]
ABS = abs(x//2-A[0])
for a in A[1:]:
    if ABS > abs(x//2-a):
        ans = a
        ABS = abs(x//2-a)
print(x,ans)