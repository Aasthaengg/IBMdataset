N,M,K=map(int,input().split())
lst=set()

for n in range(0,N+1):
    for m in range(0,M+1):
        a=n*M+m*N-n*m*2
        if a not in lst:
            lst.add(a)
print("Yes" if K in lst else "No")
