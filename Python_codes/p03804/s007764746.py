import sys


N,M=map(int,input().split())
A=[sys.stdin.readline().strip() for _ in range(N)]
B=[sys.stdin.readline().strip() for _ in range(M)]

for i in range(N-M+1):
  for j in range(N-M+1):
    As=[x[i:i+M] for x in A[j:j+M]]
    if B==As:
      print('Yes')
      sys.exit()
print('No')