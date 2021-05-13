N,M=map(int,input().split())
k_i=[]
S=[]
for i in range(M):
  l = list(map(int,input().split()))
  k_i.append(l[0])
  S.append(l[1:])
P=list(map(int,input().split()))
ans=0
for i in range(2**N):
  flag=1
  for j in range(M):
    res=0
    for k,x in enumerate(bin(i)[2:][::-1]):
      if x=="1" and k+1 in S[j]:
        res+=1
    if res%2 != P[j] :
      flag=0
      break
    
  if flag:
    ans+=1
print(ans)