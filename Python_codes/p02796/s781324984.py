N = int(input())
P = []

for _ in range(N):
    x, l = map(int,input().split())
    P.append((x - l, x+l))

P.sort(key=lambda x: x[1])

ans = 0
last = -1e9
for ix in range(0, N):
    if last <=  P[ix][0]:
        ans += 1
        last = P[ix][1]

print(ans)
