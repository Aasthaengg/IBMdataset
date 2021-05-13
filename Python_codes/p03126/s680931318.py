n,m = map(int,input().split())
A=[0]*(m+1)
for i in range(n):
    K = list(map(int,input().split()))
    for j in range(1,len(K)):
        A[K[j]]+=1
print(A.count(n))
