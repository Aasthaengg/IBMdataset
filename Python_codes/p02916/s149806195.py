N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())

ans = 0
for i in range(len(A)):
    a = A[i]
    ans += B[a-1]
    if i > 0 and A[i-1] == a - 1:
        ans += C[a-2]


print(ans)