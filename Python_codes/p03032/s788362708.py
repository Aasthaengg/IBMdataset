N,K = map(int,input().split())
V = list(map(int,input().split()))
vmax = 0
for i in range(K+1):
    for j in range(K-i+1):
        cnt = sum(V[:j])
        A = V[:j]
        n = N-(K-i-j)
        if n>=j:
            cnt += sum(V[n:])
            A += V[n:]
        else:
            cnt += sum(V[j:])
            A += V[j:]
        A = sorted(A)
        B = []
        for k in range(i):
            if k<len(A) and A[k]<0:
                B.append(k)
        for k in B:
            cnt -= A[k]
        vmax = max(vmax,cnt)
print(vmax)