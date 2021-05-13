N, K, L = [int(x) for x in input().split()]
K_lst = [[int(x) for x in input().split()] for i in range(K)]
L_lst = [[int(x) for x in input().split()] for i in range(L)]

ar = [int(i) for i in range(N + 1)]
br = [int(i) for i in range(N + 1)]

def find(x, array):
    if array[x] == x:
        return x
    else:
        array[x] = find(array[x], array)
        return array[x]

def union(x, y, array):
    x = find(x, array)
    y = find(y, array)

    if x == y:
        return
    if x > y:
        x, y = y, x
    array[y] = x

for i in K_lst:
    u, v = i
    union(u, v, ar)
for i in L_lst:
    u, v = i
    union(u, v, br)
for i in range(1, N + 1):
    find(i, ar)
    find(i, br)
dict = {}
for i in range(1, N + 1):
    a = ar[i]
    b = br[i]
    if not (a, b) in dict.keys():
        dict[(a, b)] = 1
    else:
        dict[(a, b)] += 1
a_lst = [0] * N
for i in range(N):
    a = ar[i + 1]
    b = br[i + 1]
    a_lst[i] = dict[(a, b)]
print(*a_lst)
