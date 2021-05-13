from sys import stdin
import collections

N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
A = collections.Counter(A)
for i in range(M):
    B, C = [int(x) for x in stdin.readline().rstrip().split()]
    A[C] += B 
A = dict(A)
A = dict(sorted(A.items()))

S = 0
j = -1

A_key = list(A.keys())
A_value = list(A.values())

while True:
    if A_value[j] < N:
        S += A_value[j] * A_key[j]
        N -= A_value[j]
        j -= 1
    else:
        S += N * A_key[j]
        break
print(S)
