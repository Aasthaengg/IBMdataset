def f(a,b,c):
  ans=0
  s=[0]*n
  for i in range(n):
    s[i]=l[i][0]*a+l[i][1]*b+l[i][2]*c
  s=sorted(s)
  return sum(s[n-m:n])

n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
print(max(f(1,1,1),f(1,1,-1),f(1,-1,1),f(1,-1,-1),f(-1,1,1),f(-1,1,-1),f(-1,-1,1),f(-1,-1,-1)))