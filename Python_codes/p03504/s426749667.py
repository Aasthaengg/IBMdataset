n, C = map(int, input().split())
T = 10**5
channel = []
recorder = [0 for _ in range(2*T+1)]
for loop in range(n):
    s, t, ch = map(int, input().split())
    channel.append([s, t, ch-1])

for c in range(C):
    time = [0 for _ in range(2*T+1)] # 0.5秒刻み
    for i in range(n):
        s, t, ch = channel[i]
        if ch == c:
            time[2*s-1] += 1
            time[2*t] -= 1
    for t in range(1, 2*T+1):
        time[t] += time[t-1]
    for t in range(2*T+1):
        if time[t] > 0:
            recorder[t] += 1
ans = 0
for t in range(2*T+1):
    ans = max(ans, recorder[t])
print(ans)
