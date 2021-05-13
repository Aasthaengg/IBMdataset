N=int(input())
A=list(map(int,input().split()))
a=[abs(a-sum(A)/N) for a in A]
print(a.index(min(a)))