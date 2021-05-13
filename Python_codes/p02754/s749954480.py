n,b,a = map(int,input().split())
k = n//(a+b)
p = n%(a+b)

ans = k*b+min(p,b)
print(ans)