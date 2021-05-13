N,K = map(int,input().split())
A = list(map(int,input().split()))
m = min(N,K)
M = 0 
for i in range(m+1):
    for j in range(m-i+1):
        v=A[:i]+A[N-j:]
        v.sort()
        v=v[::-1]
        h=K-len(v)
        while h >0 and v:
            if v[-1] > 0:
                break
            else:
                v.pop()
                h-=1
        M=max(M,sum(v))
print(M)