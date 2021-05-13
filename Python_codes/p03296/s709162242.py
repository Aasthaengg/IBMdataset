import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools

N,*A = map(int,read().split())

answer = 0
for _,it in itertools.groupby(A):
    x = len(list(it))
    answer += x//2

print(answer)