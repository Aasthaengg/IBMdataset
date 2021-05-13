N,K = map(int,input().split())
V = list(map(int,input().split()))
vmax = -10**9
for n1 in range(K+1):
    A = V[:n1]
    ind = min(n1,N)
    m = N-ind
    for n2 in range(min(K-n1,m)+1):
        B = V[N-n2:]
        C = A+B
        C = sorted(C,reverse=True)
        k = K-n1-n2
        for i in range(k):
            if len(C)==0 or C[-1]>=0:break
            C.pop()
        vmax = max(vmax,sum(C))
print(vmax)           