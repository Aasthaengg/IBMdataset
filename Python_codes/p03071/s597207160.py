a, b = map(int, input().split())
preans = max(a*2-1,b*2-1)
ans=max(preans,a+b)
print(ans)