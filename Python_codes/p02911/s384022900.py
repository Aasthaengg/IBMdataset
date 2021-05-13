N, K, Q = map(int,input().split())
A = [0] * N
for q in range(Q):
    a = int(input())
    A[a-1] += 1


for n in range(N):
    if (Q-A[n]) >= K:
        print('No')
    else:
        print('Yes')
