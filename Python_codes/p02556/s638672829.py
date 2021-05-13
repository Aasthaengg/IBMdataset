n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

w = [xy[i][0] - xy[i][1] for i in range(n)]
z = [xy[i][0] + xy[i][1] for i in range(n)]
print(max((max(w) - min(w)), (max(z)-min(z))))