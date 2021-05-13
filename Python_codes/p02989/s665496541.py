from math import gcd
n=int(input())
d=list(map(int,input().split()))
#昇順にソートする
d.sort()
mid_after=int(n/2)
mid_fore=mid_after-1
print(d[mid_after]-d[mid_fore])
