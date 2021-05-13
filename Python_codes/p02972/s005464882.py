import sys

N = int(input())
A = [0] + list(map(int, sys.stdin.readline().rsplit()))

res = []
M = 0
tmp = [0] * (N + 1)
for i in reversed(range(1, N + 1)):
    cnt = 0
    for j in range(i, N + 1, i):
        cnt += tmp[j]
    if cnt % 2 != A[i]:
        tmp[i] = 1
        M += 1
        res.append(i)

print(M)
if M != 0:
    print(*res[::-1])
