N=int(input())
lst=[0]
mod=10**9+7
for i in range(N):
  a=int(input())
  if lst[-1]==a:
    continue
  else:
    lst.append(a)
length=len(lst)
L=[0]*(2*10**5+1);DP=[0]*(length-1)
DP.insert(0,1)
for i in range(1,length):
  if L[lst[i]]==0:
    DP[i]=DP[i-1]%mod
    L[lst[i]]=i
  else:
    j=L[lst[i]]
    DP[i]=(DP[i-1]+DP[j])%mod
    L[lst[i]]=i
print(DP[-1])
