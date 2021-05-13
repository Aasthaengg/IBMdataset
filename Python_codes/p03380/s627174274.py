N=int(input())
L=list(map(int,input().split()))
L=sorted(list(set(L)))
M=L[-1]
K=M//2+M%2
S=[abs(i-K) for i in L]
print(M,L[S.index(min(S))])