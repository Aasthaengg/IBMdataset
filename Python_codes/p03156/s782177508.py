import numpy as np
n = int(input())
a,b = map(int, input().split())
p = np.array([int(i) for i in input().split()])
x1 = len(p[p <= a])
x2 = len(p[(a+1 <= p) & (p <= b)])
x3 = len(p[p>= b+1])
print(min(x1,x2,x3))