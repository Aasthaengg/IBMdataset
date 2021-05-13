n,m,d = map(int,input().split())
ans = (n-d)*(1+(d!=0))/n/n*(m-1)
print(ans)
