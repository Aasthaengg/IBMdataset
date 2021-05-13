n, m, x, y = map(int, input().split())
xn = [int(i) for i in input().split()]
ym = [int(i) for i in input().split()]
if max(xn) >= y:
    print("War")
elif min(ym) <= x:
    print("War")
elif max(xn) >= min(ym):
    print("War")
else:
    print("No War")