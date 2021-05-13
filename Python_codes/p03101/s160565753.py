hh, ww = map(int,input().split())
h, w = map(int,input().split())

ans = hh*ww - h*ww - w*hh + h*w

print(ans)

