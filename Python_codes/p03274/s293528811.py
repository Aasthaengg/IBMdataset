N,K = map(int,input().split())
X = list(map(int,input().split()))
A = []

for n in range(N-K+1):
  A+=[X[n+K-1]-X[n]+min(abs(X[n]),abs(X[n+K-1]))]

print(min(A))