from bisect import*
r=lambda:sorted(map(int,input().split()))
N=r()[0]
A,B,C,w,i=r(),r(),r(),[0]*(N+1),N
while i:i-=1;w[i]=w[i+1]+N-bisect(C,B[i])
print(sum(w[bisect(B,A[i])]for i in range(N)))