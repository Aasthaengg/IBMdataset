N,K=map(int,input().split())
A=list(map(int,input().split()))
p=10**9+7

cnt_self=0
for i in range(0,N-1):
  for j in range(i+1,N):
    if A[i]>A[j]:
      cnt_self += 1

cnt_each=0
for i in A:
  for j in A:
    if i>j:
      cnt_each +=1

cnt_A = (K*cnt_self)%p
cnt_B = ((K*(K-1)//2)*cnt_each)%p
ans = (cnt_A+cnt_B)%p

#print(cnt_A,cnt_B)
print(ans)