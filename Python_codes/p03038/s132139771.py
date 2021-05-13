import collections
n,m = map(int,input().split())
a = list(map(int,input().split()))
col = collections.Counter(a)
 
for i in range(m):
  b,c = map(int,input().split())
  col[c] += b
col = sorted(col.items(), key=lambda x:x[0],reverse=True)
 
ans=0
for k,v in col:
  if n <= v:
    ans += k*n
    break
  else:
    ans += k*v
    n -= v
print(ans)