import bisect

inf = 10**15
mod = 10**9+7

kouho = [111, 222, 333, 444, 555, 666, 777, 888, 999]
n = int(input())
ind = bisect.bisect_left(kouho, n)
print(kouho[ind])