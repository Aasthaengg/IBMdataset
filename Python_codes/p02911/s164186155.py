N,K,Q = map(int,input().split())
A = {}
for i in range(1,N+1):
    A[i] = 0
for i in range(Q):
    item = int(input())
    A[item] += 1
for i in range(N):
    if Q - A[i+1] >= K:
        print("No")
    else:
        print("Yes")