from bisect import bisect_right
N,K = map(int,input().split())
V = list(map(int,input().split()))
cmax = -10**9
for x in range(K+1):
    for y in range(K-x+1):
        A = V[:x]
        if y==0:
            A = sorted(A)
            ind = bisect_right(A,0)
            if ind>=K-x-y:
                cnt = sum(A[K-x-y:])
            else:
                cnt = sum(A[ind:])
            cmax = max(cmax,cnt)
        else:
            if y<=N-x:
                A += V[-y:]
                A = sorted(A)
                ind = bisect_right(A,0)
                if ind>=K-x-y:
                    cnt = sum(A[K-x-y:])
                else:
                    cnt = sum(A[ind:])
                cmax = max(cmax,cnt)
            else:
                A = sorted(V[:])
                ind = bisect_right(A,0)
                if ind>=K-N:
                    cnt = sum(A[K-N:])
                else:
                    cnt = sum(A[ind:])
                cmax = max(cmax,cnt)
print(cmax)