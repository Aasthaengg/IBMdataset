import collections
n, m = map(int, input().split())
par = [i for i in range(n)]
# print(par)
s = list()
"""
# union find(parには0も入れているので、par[1]=1になる)
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
"""


def find(x):

    while par[x] != x:
        tmp = par[x]
        par[x] = par[par[x]]
        x = par[x]

    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    else:
        par[x] = y


# 各要素をunionする
for j in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

# 1～nの親を探してsに入れていき、一番多い親を答えにする
for k in range(n):
    s.append(find(k))
# print(s)
c = collections.Counter(s)
print(max(c.values()))
