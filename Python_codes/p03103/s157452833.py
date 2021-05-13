N,M,*L=map(int,open(0).read().split());C=0
for a,b in sorted(zip(*[iter(L)]*2)):C+=a*min(M,b);M=max(M-b,0)
print(C)