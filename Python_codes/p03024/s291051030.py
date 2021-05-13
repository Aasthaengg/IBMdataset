import numpy as np

k = input()
n = [1 if i=="o" else 0 for i in k]

num = 15 - len(n)
if num >= 8-sum(n):
    print("YES")
else:
    print("NO")