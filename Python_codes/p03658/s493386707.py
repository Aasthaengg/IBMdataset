N,K=map(int,input().split())
L=list(map(int,input().split()))
L.sort(reverse=True)
sume=0
for i in range(K):
    sume+=L[i]
print(sume)