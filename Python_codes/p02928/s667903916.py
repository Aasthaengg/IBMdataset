MOD=10**9+7
N,K=map(int,input().split())
alist=list(map(int,input().split()))

b1list=alist
b2list=alist+alist

ans_k1=0
for i in range(N):
  for j in range(i+1,N):
    if b1list[i]>b1list[j]:
      ans_k1+=1
ans_k2=0
for i in range(2*N):
  for j in range(i+1,2*N):
    if b2list[i]>b2list[j]:
      ans_k2+=1      

diff_k12=ans_k2-2*ans_k1
#print(ans_k1,ans_k2,diff_k12)

answer=ans_k1*K+diff_k12*K*(K-1)//2
answer%=MOD
print(answer)