from collections import Counter
N=int(input())
A=list(map(int, input().split()))
C=Counter(A)
ct=0
for i in C:
  ct+=C[i]-1
ct+=(ct%2==1)
print(N-ct)