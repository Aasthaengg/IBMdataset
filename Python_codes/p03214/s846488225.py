N=int(input())
A=list(map(int,input().split()))
mean=sum(A)/N
S=[abs(a-mean) for a in A]
Smin=min(S)
print(S.index(Smin))