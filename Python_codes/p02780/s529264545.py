N,K=map(int,input().split())

P=list(map(int,input().split()))

probability=[]
sums=[0]
total=0
for i in range(N):
    num=0
    prob=1/P[i]
    for j in range(1,P[i]+1):
        num+=j*prob
    probability.append(num)
    total+=num
    sums.append(total)

ans=0
for j in range(N-K+1):
    if ans<sums[j+K]-sums[j]:
        ans=sums[j+K]-sums[j]

print('{:.012f}'.format(ans))