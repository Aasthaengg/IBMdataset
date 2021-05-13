from operator import itemgetter

n, m = map(int, input().split())
youbou = [tuple(map(int, input().split())) for _ in range(m)]
ab = sorted(youbou, key=itemgetter(1))

ans = 0
removed = 0

for a, b in ab:
    if a >= removed:
        ans += 1
        removed = b  # b島の直前の橋を取り除く

print(ans)