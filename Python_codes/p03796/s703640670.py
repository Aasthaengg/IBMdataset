N=int(input())
M=10**9+7
K=1

for i in range(1,N+1):
    K=(K*i)%M
print(K)
