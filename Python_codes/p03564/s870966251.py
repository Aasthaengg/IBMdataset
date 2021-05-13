from itertools import product
n = int(input())
k = int(input())
m = float('inf')
for i in product(['*2', '+k'], repeat=n):
    m = min(m, eval('1'+''.join(i)))
print(m)