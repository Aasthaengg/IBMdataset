N = int(input())
K = int(input())
ball_list = list(map(int, input().split()))

ans = 0

for ball in ball_list:
    if abs(ball - 0) <= abs(ball - K):
        ans += abs(ball - 0) * 2
    else:
        ans += abs(ball - K) * 2

print(ans)
