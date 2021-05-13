N, M = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))
ans = 0

for i in range(1<<N):
    on = 0
    onoff = bin(i)[2:].zfill(N)
    for j, switches in enumerate(lights):
        if sum(onoff[s-1] == '1' for s in switches[1:]) % 2 == p[j]:
            on += 1
    if on == M:
        ans += 1

print(ans)