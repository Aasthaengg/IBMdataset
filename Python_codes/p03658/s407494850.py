N,K=map(int,input().split())
L=list(map(int,input().split()))
M=(sorted(L))
A=M[::-1]
print(sum(A[:K]))