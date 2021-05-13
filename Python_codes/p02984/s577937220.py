N=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
mt=[0]*N

for j in range(N-1):
    mt[j+1]=arr[j]*2-mt[j]
a=total-sum(mt)

for i in range(N):
    if i%2==0:
        mt[i]+=a
    else:
        mt[i]-=a
        
print(*mt)