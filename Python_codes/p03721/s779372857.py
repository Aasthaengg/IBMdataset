N, K = map(int,input().split())

A = [0] * (10**5)

for i in range(N):
    a,b = map(int,input().split())
    A[a-1] += b

cnt = 0
while K > 0:
    K -= A[cnt]
    cnt += 1
print(cnt)