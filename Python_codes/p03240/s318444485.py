N=int(input())
lst=[0 for f in range(N)]
for i in range(N):
 lst[i]= list(map(int,input().split()))
lst.sort(key=lambda x: x[2], reverse=True)
for i in range(101):
 for j in range(101):
  h=abs(i-lst[0][0])+abs(j-lst[0][1])+lst[0][2]
  if h==10**9 and N==1:
   ans=[lst[0][0],lst[0][1],lst[0][2]]
  else:
   t=0
   for k in range(N-1):
    if max(h-abs(i-lst[k+1][0])-abs(j-lst[k+1][1]),0)==lst[k+1][2]:
     t+=1
   if t==N-1:
    ans=[i,j,h]
print(*ans)
