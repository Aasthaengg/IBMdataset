n,m,d = map(int,input().split())

nxt = 1/n
if 2*d+1 <= n and d >= 1:
  nxt += (n-2*d)/n**2
#print(nxt)
ans = nxt*(m-1)
print(ans)