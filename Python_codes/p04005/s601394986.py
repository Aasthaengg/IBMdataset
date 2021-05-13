a,b,c = map(int,input().split())
ans = min(a*b,b*c,c*a)
x = max(a,b,c)
print (0) if x%2 == 0 else print (ans)
