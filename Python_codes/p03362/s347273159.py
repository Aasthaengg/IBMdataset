# ABC096D
from itertools import combinations
def hurui(n):
    """n以下の素数のリストを返す
    """
    l = list(range(2,n))
    p = 2
    i = 0
    while True:
        l = [item for item in l if item==p or item%p!=0]
        i += 1
        p = l[i]
#         print(p)
        if p*p>n:
            break
    return l

n = int(input())
ps = hurui(55555*5)
is_prime = [False] * 55555*5
for item in ps:
    is_prime[item] = True
l = []
for p in ps:
    if p%5==2:
        l.append(p)
    if len(l)==n:
        break
print(*l)