(a,b) = map(int,input().split())
ans = a+a-1
ans = max(ans,b+b-1)
ans = max(ans,a+b)
print(ans)