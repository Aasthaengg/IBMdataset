from bisect import bisect_left

n, m, x = map(int, input().split())
alst = list(map(int, input().split()))
pos = bisect_left(alst, x)
print(min(pos, m - pos))