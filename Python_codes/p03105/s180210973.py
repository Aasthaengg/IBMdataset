a,b,c = map(int,input().split())
ans = b // a
if ans >= c: print(c)
else: print(ans)