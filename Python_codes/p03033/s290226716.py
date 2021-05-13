from bisect import bisect_left
from operator import itemgetter
import sys

input = sys.stdin.readline

N, Q = map(int, input().split(" "))
check_points = [tuple(map(int, input().split(" "))) for _ in range(N)]
querys = [int(input()) for _ in range(Q)]
time = [-1] * Q
jump = [-1] * Q
check_points = sorted(check_points, key=itemgetter(2))
b_left = bisect_left

for line in check_points:
    s, f, x = line
    start = s-x
    end = f-x
    left = b_left(querys, start)
    right = b_left(querys, end)
    while left < right:
        if time[left] == -1:
            time[left] = x
            jump[left] = right
            left += 1
        else:
            left = jump[left]

for t in time:
    print(t)
