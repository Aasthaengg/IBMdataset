A,B,K=list(map(int, input().split()))
a=min(A+K-1,B)
b=max(A,B-K+1)
L=list(range(A,a+1)) + list(range(b,B+1))
L=list(set(L))
L.sort()
for _ in range(len(L)):
  print(L[_])