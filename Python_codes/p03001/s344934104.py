w,h,x,y=map(int, input().split())
S= w*h/2
ans = 1 if (x+x==w) and (y+y==h) else 0
print(S, ans)