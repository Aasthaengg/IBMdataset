N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
pre_ai = A[0]
for i in range(1, N):
    ai = A[i]
    over = max(pre_ai + ai - x, 0)
    ans += over
    pre_ai = max(ai - over, 0)
print(ans)