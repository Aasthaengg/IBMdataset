import sys
input = sys.stdin.readline


n, c = map(int, input().split())
tv_guide = []
for _ in range(n):
    start, end, channel = map(int, input().split())
    tv_guide.append([start, 1, channel-1])
    tv_guide.append([end, 0, channel-1])

tv_guide.sort(key=lambda x:(x[0], -x[1]))

channel_count = [0] * c
channel_set = set()
ans = 0
for time, on, channel in tv_guide:
    if on:
        channel_set.add(channel)
        channel_count[channel] += 1

    else:
        channel_count[channel] -= 1
        if channel_count[channel] == 0:
            channel_set.discard(channel)

    candidate = len(channel_set)
    if ans < candidate:
        ans = candidate

print(ans)