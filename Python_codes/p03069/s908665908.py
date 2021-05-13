import numpy as np
def f(lst):
    return np.cumsum(lst)

n = int(input())
s = input()

res1 = s.count('.')
res2 = s.count('#')

a = [0]*n
b = [0]*n

for i in range(n):
    if s[i]=='.':
        a[i] += 1
    else:
        b[i] += 1
cum_a = f(a).tolist()
cum_b = f(b).tolist()
res3 = np.inf
for i in range(n):
    if a[i]==1:
        res3 = min(res3, cum_b[i]+(res1-cum_a[i]))

print(min(res1, res2, res3))