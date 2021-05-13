N,K = map(int,input().split())
if K%2:
    tmp = len(range(K,N+1,K))
    print(tmp**3)
else:
    tmp = len(range(K//2,N+1,K))
    tmp2 = len(range(K,N+1,K))
    print(tmp**3+tmp2**3)