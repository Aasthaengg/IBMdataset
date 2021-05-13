import sys
input = sys.stdin.readline
n,c = map(int, input().split())
channels = {i:[] for i in range(1,c+1)}
table = [0 for _ in range(200004)]
for _ in range(n):
    s,t,c = map(int, input().split())
    channels[c].append([s,t])

for ch, time in channels.items():
    sub = [0 for _ in range(200004)]
    for s,t in time:
        if sub[s*2]:
            sub[s*2] = 0
        else:
            sub[s*2-1] = 1
        if sub[t*2-1]:
            sub[t*2-1] = 0
        else:
            sub[t*2] = -1
    for i in range(1,200002):
        sub[i] += sub[i-1]
        table[i] += max(0, sub[i])
ans = 0
for i in range(1,200002):
    ans = max(ans, table[i])
print(ans)
