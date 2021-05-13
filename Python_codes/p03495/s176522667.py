n, k = map(int, input().split())
a = map(int, input().split())
ball_count = {}
for num in a:
    if num in ball_count:
        ball_count[num] += 1
    else:
        ball_count[num] = 1
ball_kinds = len(ball_count.keys())
ball_count_list = sorted(ball_count.values(), reverse=True)
ans = 0
for _ in range(ball_kinds - k):
    ans += ball_count_list.pop()

print(ans)
