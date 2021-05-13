import bisect

n = int(input())
a = list(map(int,input().split()))
a.sort()

# 確定
last = a[-1]
a = a[:-1]

first = 10**10
now = 10**10

for i in a:
    m = min(abs(i-last//2),abs(i-(last+1)//2))
    if now > m:
        now = m
        first = i

print(last,first)