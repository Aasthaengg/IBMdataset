N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ans = 0
for i, a in enumerate(A):
    b = B[a-1]
    ans+=b
    if a-1 == A[i-1] and i-1>=0:
        ans+=C[a-2]
print(ans)