w, h, x, y = map(int, input().split())
ans = (w * h) / 2
if w/2 == x and h/2 == y:
    print(str(ans) + ' 1')
else:
    print(str(ans) + ' 0')