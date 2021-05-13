N=int(input())
a=list(map(int,input().split()))

K=0
for i in range(N):
    if a[a[i]-1]==i+1:
        K+=1
print(K//2)