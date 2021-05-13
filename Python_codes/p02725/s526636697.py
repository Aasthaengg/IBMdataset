K,N = map(int,input().split())
A = list(map(int,input().split()))
cmin = K-(K-A[-1]+A[0])
for i in range(1,N):
    cmin = min(cmin,K-(A[i]-A[i-1]))
print(cmin)