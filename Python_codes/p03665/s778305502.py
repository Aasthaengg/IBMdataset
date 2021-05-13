def fur(n, r):
    return  math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
import math
n, p = map(int, input().split())
A = list(map(lambda x:int(x)%2, input().split()))
from collections import Counter
c = dict(Counter(A))
a, b = 0, 0
if c.get(0) != None:
    a = c[0]
if c.get(1) != None:
    b = c[1]
result = 0
piyo = 1
for i in range(1, a+1):
    piyo += fur(a, i)
for i in range(0, b+1, 2):
    result += fur(b, i) * piyo
if p == 0:
    print(result)
else:
    hoge = 0
    for i in range(n+1):
        hoge += fur(n, i)
    print(hoge - result)
