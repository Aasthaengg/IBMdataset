# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# しゃくとり法
N = ir()
A = lr()
answer = 0
left = 0
right = 0

temp = A[left]
while left < N:
    while right < N-1:
        num = A[right+1]
        if temp ^ num != temp + num:
            break
        temp += num
        right += 1
    right = max(right, left)
    answer += right - left + 1
    temp -= A[left]
    left += 1

print(answer)
