# coding: utf-8
# Your code here!
from collections import deque

N = int(input())
a = deque(list(map(int, input().split())))
tmp_a = []
tmp_c = 0
tmp_n = 0
ctr = 0

for i in range(N):
    tmp_n = a.popleft()
    if tmp_a == [] or tmp_a[-1] == tmp_n:
        tmp_c += 1
    else:
        ctr += tmp_c // 2
        tmp_c = 1
        tmp_a.clear()
    tmp_a.append(tmp_n)
    if a == deque([]) and tmp_a[-1] == tmp_n:
        ctr += tmp_c // 2
print(ctr)