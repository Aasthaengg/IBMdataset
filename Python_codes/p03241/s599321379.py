from math import sqrt
from bisect import bisect_left

N,M = map(int,input().split())


t = M
#約数全列挙
for i in range(1,int(sqrt(M))+2,1):
    if M % i ==0:
        count = 0
        if M % i == 0:
            if N <= i and i <= t:
                t = i
            if N <= M//i and M//i <= t:
                t = M//i

print(M//t)