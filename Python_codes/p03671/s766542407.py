a,b,c = map(int,input().split())
ans = a+b+c
ans = ans - max(a,b,c)
print(ans)