N, K = map(int, input().split())
*x, = map(int, input().split())
ans = float('inf')
for i in range(N-K+1):
    chk = 0
    left = x[i]
    right = x[i+K-1]
    left_to_right = abs(left - right) + abs(left)
    right_to_left = abs(right-left) + abs(right)
    chk = min(left_to_right, right_to_left)
    ans = min(ans, chk)
print(ans)