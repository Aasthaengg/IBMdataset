# -*- coding: utf-8 -*-
#D - Static Sushi 
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))

right = 0
ans = 0
total = 0
#尺取法 閉区間
for left in range(N):
    while right < N and (total ^ A[right]) == (total + A[right]):
        total += A[right]
        right += 1
    ans += right-left
    if left == right:
        right += 1
    else:
        total -= A[left]
print(ans)