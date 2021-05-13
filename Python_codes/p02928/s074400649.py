N,K=input().split()
N,K=int(N),int(K)
A=input().split()

A=[int(N) for N in A]

prev=0
foll=0
for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            prev+=1
    for j in range(i,N):
        if A[i]>A[j]:
            foll+=1

a = (K*(K-1)//2)%(10**9+7)
b = foll*K%(10**9+7)
u= (prev+foll)*a+b
print(u%(10**9+7))