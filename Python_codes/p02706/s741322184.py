N,M=map(int,input().split())
A=list(map(int, input().split()))

r = N-sum(A)
if r < 0:r=-1
print(r)