n , k = map(int, input().split())

li = [0]*(n+2)
lis = []
lr=[]
lis2 =[0]*(3*n)
lis2[1]=1
lis2[2]=-1

for i in range(k):
    l,r = map(int, input().split())
    lr.append((l,r))

for i in range(1,n+1):
    lis2[i]+=lis2[i-1]
    lis2[i]%=998244353

    for j,k in lr:
        lis2[i+j]+=lis2[i]
        lis2[i+k+1]-=lis2[i]

print(lis2[n]%998244353)
