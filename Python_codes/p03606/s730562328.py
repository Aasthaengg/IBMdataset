# -*- coding: utf-8 -*-

#----------
N = int(input().strip())
#----------

sum=0
for i in range(N):
    l,r = list(map(int, input().rstrip().split()))
    sum += r - (l-1)

print(sum)
