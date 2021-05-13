h,w,n=map(int,input().split())
jl=[0]*10
cnt={}
if n==0:
  print((w-2)*(h-2))
  for i in range(9):
    print(0)
  exit()
for i in range(n):
  a,b=map(int,input().split())
  a-=1
  b-=1
  for j in range(max(0,b-2),min(w-2,b+1)):
    for k in range(max(0,a-2),min(h-2,a+1)):
      if (k, j) in cnt:
        cnt[(k, j)]+=1
      else:
        cnt[(k, j)]=1
jl[0]=(h-2)*(w-2)
for i in cnt.values():
  jl[0]-=1
  jl[i]+=1
for i in jl:
  print(i)