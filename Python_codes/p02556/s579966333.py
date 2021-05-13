N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XplusY = [x + y for x, y in XY]
XminusY = [x - y for x, y in XY]

print(max([max(XplusY) - min(XplusY), max(XminusY) - min(XminusY)]))
