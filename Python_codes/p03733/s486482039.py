n, time = map(int, input().split())
T = list(map(int, input().split()))

cnt = time
tmp = T[0]
for t in T[1:]:
    if t <= tmp + time:
        cnt += t - tmp
    else:
        cnt += time
    tmp = t

print(cnt)