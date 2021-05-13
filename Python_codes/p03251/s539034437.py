n, m, x, y = map(int, input().split())
xx = list(map(int, input().split()))
yy = list(map(int, input().split()))
xxx = max(xx + [x])
yyy = min(yy + [y])
if xxx < yyy:
    print("No War")
else:
    print("War")
