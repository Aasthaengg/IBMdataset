n, m, x, y = map(int, input().split())
xw = list(map(int, input().split()))
yw = list(map(int, input().split()))
xm = max(x, max(xw))
ym = min(y, min(yw))
if xm < ym:
    print("No War")
else:
    print("War")