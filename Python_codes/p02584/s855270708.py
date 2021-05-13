# -*- coding: utf-8 -*-
x, k, d = map(int, input().split())
x = abs(x)
t = x // d
if t >= k:
    answer = x - (k * d)
else:
    if (k - t) % 2 == 0:
        answer = x - (t * d)
    else:
        answer = x - (t + 1) * d
        
print(abs(answer))