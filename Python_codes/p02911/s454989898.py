# C - Attack Survival
N,K,Q = map(int,input().split())
P = [0]*N
for _ in range(Q):
    A = int(input())
    P[A-1] += 1
for p in P:
    print('Yes' if K-Q+p>0 else 'No')