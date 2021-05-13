N,K,Q = map(int, input().split())
li = [0 for i in range(N)]
for i in range(Q):
    a = int(input())
    li[a-1] += 1
for i in range(N):
    if K - (Q-li[i]) <= 0:
        print('No')
    else:
        print('Yes')