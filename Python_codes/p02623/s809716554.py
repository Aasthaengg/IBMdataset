n,m,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a,b = [0],[0]
for i in range(n):
  a.append(a[i]+A[i])
for i in range(m):
  b.append(b[i]+B[i])
  
ans,bi = 0,m
for i in range(n+1):
  for j in range(bi,-1,-1):
    if a[i]+b[j]<=k:
      ans = max(ans,i+j)
      bi = j
      break
print(ans)