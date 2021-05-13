#C - Attack Survival
N,K,Q = map(int,input().split())
A = list(int(input()) for i in range(Q))
score = [0]*(N)
for i in range(Q):
    score[A[i]-1] += 1
score = [(K-Q+j) for j in score]
for k in score:
    if k > 0:
        print('Yes')
    else:
        print('No')