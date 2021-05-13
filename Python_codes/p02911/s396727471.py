N,K,Q = map(int,input().split())
A = [0]*Q
for i in range(Q):
    A[i] = int(input())
    

points = [K-Q]*N
for i in range(Q):
    points[A[i]-1] += 1
for i in range(N):
    if points[i]<=0:
        print('No')
    else:
        print('Yes')