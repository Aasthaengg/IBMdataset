N,K=map(int,input().split())
A=list(map(int,input().split()))
num=[0 for i in range(N)]
for i in range(N):
    num[A[i]-1]+=1

num.sort()
sum=0
for i in range(N-K):
    sum+=num[i]

print(sum)
