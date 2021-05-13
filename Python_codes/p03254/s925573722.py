# -*- coding: utf-8 -*-

N,x = map(int, input().split())
a = list(map(int, input().split()))

a_sorted = sorted(a)

num = 0
reminder = x
for i in range(N):
    reminder -= a_sorted[i]
    if reminder>=0:
       num += 1
    else:
        break

if reminder>0:
    num -= 1
    
print(num)
