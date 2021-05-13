N,K = map(int,input().split())
A = []
for i in range(N):
    a,b = map(int,input().split())
    A.append([a,b])
A.sort()

for i in range(N):
    K = K - A[i][1]
    if K <= 0:
        print(A[i][0])
        exit(0)
