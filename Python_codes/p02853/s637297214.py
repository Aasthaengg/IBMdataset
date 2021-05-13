# coding: utf-8

x, y = map(int,input().split())

l1 = [1,2,3]
l2 = [300000,200000,100000]

ans = 0
if x in l1:
    ans += l2[l1.index(x)]
    
if y in l1:
    ans += l2[l1.index(y)]

if x == 1 and y == 1:
    ans += 400000

print(ans)