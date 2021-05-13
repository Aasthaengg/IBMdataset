import itertools
n = int(input())

ans = [0] * n
for v in itertools.product(list(range(1,101)), repeat=3):
    x,y,z = v[0], v[1], v[2]
    a = x*x + y*y + z*z + x*y + y*z + z*x
    if a <= n:ans[a-1] += 1
    else: continue
for i in ans: print(i)