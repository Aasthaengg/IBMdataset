N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    ans += B[a-1]
    if i != 0 and a == A[i-1] +1:
        ans += C[a-2]

print(ans)
