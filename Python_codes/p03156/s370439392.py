n, a, b, *P = map(int, open(0).read().split())
cnt = [0]*3
for p in P:
    if p <= a:
        cnt[0] += 1
    elif a < p <= b:
        cnt[1] += 1
    else:
        cnt[2] += 1
print(min(cnt))
