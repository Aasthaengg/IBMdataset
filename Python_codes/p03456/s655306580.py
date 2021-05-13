import math

s = input().split()
a = s[0]
b = s[1]

answer = False

v = int(a + b)

w = int(math.sqrt(v))

if w * w == v:
    answer = True

if answer:
    print('Yes')
else:
    print('No')





