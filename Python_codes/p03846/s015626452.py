import sys
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
mod = 10 ** 9 + 7
count = Counter(A)
flag = 0
if N % 2 == 0:
    for i in range(1, N, 2):
        if count[i] != 2:
            flag = 1
else:
    if count[0] != 1:
        flag = 1
    for i in range(2, N, 2):
        if count[i] != 2:
            flag = 1
if flag:
    print(0)
else:
    print((2 ** (N // 2)) % mod)