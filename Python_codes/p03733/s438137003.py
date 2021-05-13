n,T = map(int, input().split())
ts = list(map(int, input().split()))

prev = ts[0]
cnt = 0
for t in ts[1:]:
    # print(t,prev)
    cnt += min(T, t - prev)
    prev = t
print(cnt+T)