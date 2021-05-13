N,K,Q = map(int,input().split())
points = [0] * (N+1)
for i in range(Q):
    a = int(input())
    points[a] += 1
for i in range(1,N+1):
    if points[i] + K > Q:
        print('Yes')
    else:
        print('No')