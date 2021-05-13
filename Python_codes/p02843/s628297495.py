import math
a = input()
X = int(a)

b = X // 100

if b*100 <= X and X <= b*105:
    print(1)
else:
    print(0)
