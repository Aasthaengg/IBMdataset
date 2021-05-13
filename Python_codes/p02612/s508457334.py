N = int(input())
import math as m
a = m.ceil(N / 1000)
ans = int(a*1000 - N)
print(ans)