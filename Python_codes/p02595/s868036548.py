N, D = (int(x) for x in input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
i = cnt = 0


DS = D * D

while i < N:
    if x[i]**2 + y[i]**2 <= DS:
        cnt += 1
    i += 1

print(cnt)