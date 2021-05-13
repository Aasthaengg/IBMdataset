N,L = map(int,input().split())
fabs = [abs(L+i-1) for i in range(1,N+1)]
f = [(L+i-1) for i in range(1,N+1)]
print(sum(f)-f[fabs.index(min(fabs))])
