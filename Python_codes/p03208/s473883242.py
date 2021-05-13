N,K = map(int,input().split())
H = sorted([int(input()) for n in range(N)])
A = []

for n in range(N-K+1):
  A+=[H[n+K-1]-H[n]]

print(min(A))