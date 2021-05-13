# backfront
N = int(input())
a = []
for _ in range(N):
    x = int(input())
    a.append((_, x))
a.sort(key=lambda x: x[1])
a.append((-10000000000000000, 10**20))
cnt, now, maxi = 0, -1, 0
for p, v in a:
    if now < p:
        cnt += 1
        now = p
    elif now > p:
        maxi = max(maxi, cnt)
        cnt = 1
        now = p
print(N-maxi)