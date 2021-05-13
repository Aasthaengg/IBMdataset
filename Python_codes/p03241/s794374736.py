N, M = map(int, input().split())

d = 1
ds = []
while d ** 2 <= M:
    if M % d == 0:
        ds.append(d)
        ds.append(M // d)
    d += 1
ds.sort(reverse=True)
for d in ds:
    if N * d <= M:
        print(d)
        break