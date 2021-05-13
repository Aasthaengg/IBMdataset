N,A,B,C=map(int,input().split())
lst=[int(input()) for i in range(N)]
key=4**N
ans=float("inf")
for i in range(4**N):
 flg=[0]*N 
 for j in range(N):
  if i!=0:
   flg[j]=i%4
  i=int(i/4)
 TA=0
 TB=0
 TC=0
 TD=0
 for k in range(N):
  if flg[k]==0:
   TA+=lst[k]
  elif flg[k]==1:
   TB+=lst[k]
  elif flg[k]==2:
   TC+=lst[k]
  else:
   TD+=1
  if TA!=0 and TB!=0 and TC!=0 :
   ans=min((N-TD-3)*10+abs(A-TA)+abs(B-TB)+abs(C-TC),ans)
print(ans)
