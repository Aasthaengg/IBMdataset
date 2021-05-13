n=int(input())
ss=list(input())
res= ss.count('R') * ss.count('G') * ss.count('B')
for i in range(n):
  for j in range(i+1,n):
    k = 2*j-i
    if k >= n:
      continue
    if all([ss[i] != ss[j],ss[j] != ss[k],ss[k] != ss[i]]):
      res-=1
print(res)