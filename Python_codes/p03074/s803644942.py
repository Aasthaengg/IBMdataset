N,K=map(int,input().split())
S=input()
if N==1:
 print(1)
else:
 lst=[]
 ct=1
 if int(S[0])==0:
  lst.append(0)
 ima=int(S[0])
 for i in range(1,N):
  if int(S[i])==ima:
   ct+=1
  else:
   lst.append(ct)
   ima=int(S[i])
   ct=1
 lst.append(ct)
 if ima==0:
  lst.append(0)
 A=len(lst)-2
 if A<=K*2-1:
  print(N)
 else:
  for i in range(1,len(lst)):
   lst[i]+=lst[i-1]
  ans=0
  for i in range((len(lst)-1-2*K)//2+1):
   if i==0:
    ans=max(ans,lst[2*i+2*K])
   else:
    ans=max(ans,lst[2*i+2*K]-lst[2*i-1])
  print(ans)