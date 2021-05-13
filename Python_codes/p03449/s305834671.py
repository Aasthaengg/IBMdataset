N=int(input())
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
cnt=[]
for i in range(N):
  cnt.append(sum(L1[:i+1])+sum(L2[i:]))
ans=max(cnt)
print(ans)