import itertools
n, t = map(int,input().split())
tl = list(map(int,input().split()))

water = 0
for i in range(1,n):
    diff = tl[i]-tl[i-1]
    if diff <= t:
        water += diff
    else:
        water += t
water += t
print(water)