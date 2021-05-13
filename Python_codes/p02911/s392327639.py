import collections

N,K,Q = map(int,input().split())
A = [int(input()) for i in range(Q)]
c = collections.Counter(A)

if (K - Q) > 0:
    for _ in range(N):
        print('Yes')
else:
    l = ['No'] * N
    for i,v in dict(c).items():
        if v >(Q - K):
            l[i-1] = 'Yes'
    for j in l:
        print(j)