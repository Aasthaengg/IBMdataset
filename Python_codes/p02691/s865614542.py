from collections import Counter

N = int(input())
A = list(map(int, input().split()))

#cnt = 0
#for i in range(N):
#  for j in range(i, N):
#    if j - i == A[i] + A[j]:
#      cnt += 1

Ap = [A[i]+i for i in range(len(A))]
Am = [i-A[i] for i in range(len(A))]

S = set(Ap) & set(Am)

Cp = Counter(Ap)
Cm = Counter(Am)

cnt = 0
for i in S:
  cnt += Cp[i]*Cm[i]
  
print(cnt)