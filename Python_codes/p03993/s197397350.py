N = int(input())
A = [int(i)-1 for i in input().split()]

from collections import defaultdict

flag = [True] * N

cnt = 0
for i in range(N):
    if flag[A[i]] and flag[i] and A[A[i]] == i:
        cnt += 1
        flag[A[i]] = False
        flag[i] = False

print(cnt)