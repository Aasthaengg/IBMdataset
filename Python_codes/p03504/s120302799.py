T_max = 10**5
N, C = map(int, input().split())
channel = [[] for _ in range(C)]
time = [0]*(T_max+2)
for i in range(N):
    s, t, c = map(int, input().split())
    channel[c-1].append((s, t))
for c in channel:
    c.sort()
    if len(c)==0:
        continue
    time[c[0][0]]+=1
    for i in range(1, len(c)):
        if c[i-1] [1] != c[i][0]:
            time[c[i-1][1]+1] -= 1
            time[c[i][0]]+=1
    time[c[-1][1]+1]-=1
for i in range(1, T_max+1):
    time[i] = time[i-1]+time[i]
print(max(time))