h,w,n=map(int,input().split())
dic={}
INF=10**10
for i in range(n):
  y,x=map(int,input().split())
  for j in range(max(2,x-1),min(w-1,x+1)+1):
    for k in range(max(2,y-1),min(h-1,y+1)+1):
      if j*INF+k in dic:
        dic[j*INF+k]+=1
      else:
        dic[j*INF+k]=1
ans=[0]*10
ans[0]=(h-2)*(w-2)
for i in dic:
  ans[0]-=1
  ans[dic[i]]+=1
for i in ans:
  print(i)
