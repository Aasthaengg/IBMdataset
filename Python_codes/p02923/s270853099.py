N=int(input())
L=[0]+list(map(int, input().split()))+[10**9+7]
ct=0
ans=0
for i in range(1,N+2):
  if L[i-1]>=L[i]:
    ct+=1
  else:
    ans=max(ans,ct)
    ct=0
print(ans)