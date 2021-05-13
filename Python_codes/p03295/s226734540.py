N, M = map(int,input().split())
bridges = []
for _ in range(M):
    bridges.append(list(map(int,input().split())))
bridges = sorted(bridges, key=lambda x: x[1])
MAX = 0
ans = 0
for a, b in bridges:
    if a > MAX:
        ans += 1
        MAX = b-1
print(ans)