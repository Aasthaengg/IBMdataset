#ABC 074 B

N = int(input())
K = int(input())
x = list(map(int,input().split()))

cnt = 0

for i in range(N):
    if abs(x[i]-0) > abs(x[i]-K):
        cnt += 2* abs(x[i]-K) 
    else:
        cnt += 2*x[i]
print(cnt)