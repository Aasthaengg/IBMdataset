a,b,c = map(int,input().split())
ans = min(b+c,c+b,a+c,c+a,a+b,b+a)
print(ans)