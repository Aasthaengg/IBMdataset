A,B,K = map(int,input().split())

W = list(range(A,min(A+K,B+1)))
w = list(range(max(A,B-K+1),B+1))

A = sorted(set(W+w))
for i in A: print(i)