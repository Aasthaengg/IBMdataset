import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x,y = map(int, input().split())
l = [(sx*x, sy*y, (sx==-1)+(sy==-1)) for sx in (-1,1) for sy in (-1,1)]
ans = float("inf")
for lx, ly,v in l:
    if lx<=ly:
        ans = min(ans, ly-lx+v)
print(ans)
# if 0<=x<y:
#     ans = y-x
# elif x<y<=0:
#     ans = y-x
# elif x<=0<=y:
#     if abs(x)<=abs(y):
#         ans = min(y-x, 1+abs(y)-abs(x))
#     else:
#         ans = y-x
# elif 0<=y<x:
#     ans = min(1 + y + x, 1 + abs(x)-abs(y) + 1)
# elif y<x<=0:
#     ans = min(1 + (-y) + (-x), 1 + abs(y)-abs(x) + 1)
# elif y<=0<=x:
#     ans = abs(abs(x)-abs(y)) + 1