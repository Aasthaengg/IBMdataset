N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
# 単価が安い順に店を並べる
sorted_AB = sorted(AB, key=lambda x: x[0])

money = 0
cnt = 0
for a, b in sorted_AB:
    tmp = min(b, M - cnt)
    cnt += tmp
    money += a * tmp
    if cnt == M:
        break
print(money)
