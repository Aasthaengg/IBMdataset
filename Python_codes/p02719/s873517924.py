# coding: utf-8
n, k = map(int, input().split())
x1 = n % k
x2 = k - x1
if x1 < x2:
    print(x1)
else:
    print(x2)
    
