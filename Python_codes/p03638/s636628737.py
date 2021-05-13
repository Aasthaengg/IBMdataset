h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
s=[0]*n
for i in range(n):
  s[i]=s[i-1]+a[i]
s=[0]+s
c=[[0]*w for _ in range(h)]
cnt=0
k=1
for i in range(h):
  for j in range(w):
    cnt+=1
    if cnt>s[k]:
      k+=1
    if i%2==0:
      c[i][j]=k
    else:
      c[i][w-1-j]=k
for c_y in c:
  print(*c_y)