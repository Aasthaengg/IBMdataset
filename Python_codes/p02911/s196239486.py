import collections
N,K,Q = list(map(int,input().split()))
A = [ int(input()) for i in range(Q)]
cnt = collections.Counter(A)
ini_po = [K]*N
fi_po =[]
for i in range(N):
    t_po = ini_po[i]
    if i+1 in cnt:
        t_po += -Q + cnt[i+1]
    else:
        t_po -= Q
    if t_po >0:
        print('Yes')
    else:
        print('No')
