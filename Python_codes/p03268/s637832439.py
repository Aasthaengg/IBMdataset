import sys
def input():
  return sys.stdin.readline().rstrip()

N,K=map(int,input().split())

num_=[0]*K
for i in range(1,N+1):
  num_[i%K]+=1
ans=0
for a in range(K):
  b=(K-a)%K
  c=(K-a)%K
  if (b+c)%K!=0:
    continue
  ans+=num_[a]*num_[b]*num_[c]

print(ans)
