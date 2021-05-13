from collections import Counter
N = int(input())
A = list(map(int,input().split()))

if N%2 == 0:
  B = list(range(N-1,0,-2))+list(range(1,N,2))
else:
  B = list(range(N-1,0,-2))+list(range(0,N,2))

if Counter(A) != Counter(B):
  print(0)
else:
  mod = 10**9+7
  print(2**(N//2)%mod)