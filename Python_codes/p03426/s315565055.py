h,w,d=map(int,input().split())
n=h*w
a=[None for i in range(n)]
for i in range(h):
  inp=list(map(int,input().split()))
  for j in range(w):
    a[inp[j]-1]=(i,j)

dst=[0 for i in range(d)]
for i in range(d,n):
  dst.append(abs(a[i-d][0]-a[i][0])+abs(a[i-d][1]-a[i][1]))

s=[0 for i in range(d)]
for i in range(d,n):
  s.append(s[i-d]+dst[i])

  
  
q=int(input())
for i in range(q):
  l,r=map(int,input().split())
  print(s[r-1]-s[l-1])