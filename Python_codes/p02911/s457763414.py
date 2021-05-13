N,K,Q=map(int,input().split())
A=[0]*N
for _ in range(Q):
    A[int(input())-1]+=1
p=[K-Q]*N

for a,b in zip(A,p):
    print('Yes' if 0<a+b else 'No')