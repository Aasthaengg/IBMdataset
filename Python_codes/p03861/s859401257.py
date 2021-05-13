a,b,x = map(int,input().split())
ans = b // x
a-=1
ans -= (a // x)
print(ans)