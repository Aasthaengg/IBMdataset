from bisect import bisect_right
from itertools import accumulate

n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr = list(accumulate(arr))


happy = bisect_right(arr, x)

if happy == n:
    if arr[-1] != x:
        happy -= 1

print(happy)