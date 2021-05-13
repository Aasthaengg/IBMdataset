import collections

N, M = map(int,input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = input().split()
C = A + B
D = collections.Counter(C)
for i in D:
    if D[i] % 2 == 0:
        continue
    else:
        print('NO')
        exit()
print('YES')
