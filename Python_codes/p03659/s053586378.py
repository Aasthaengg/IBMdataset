N = int(input())
A = list(map(int,input().split()))
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = B[i-1]+A[i-1]
cmin = 10**15
for i in range(1,N):
    cmin = min(cmin,abs(2*B[i]-B[N]))
print(cmin)