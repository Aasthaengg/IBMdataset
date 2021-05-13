import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, a, b = map(int, input().split())
vs = list(map(int, input().split()))
vs.sort(reverse=True)
rsw = [0]*(n+1)
for i in range(1,n+1):
    rsw[i] = sum(vs[:i])/i
#print(vs)
#print(rsw)
res = -float('inf')
for i in range(a,b+1):
    res = max(res,rsw[i])
print(res)
mut = []
res_lists = []
for i in range(1,b+1):
    if i < a:
        mut.append(vs[i-1])
    elif i == a:
        res_lists.append(mut.copy()+[vs[i-1]])
    else:
        if rsw[i] < res:
            break
        res_lists.append(res_lists[-1].copy() + [vs[i - 1]])
#print(res_lists)
res = 0
for lis in res_lists:
    x = lis[-1]
    r = lis.count(x)
    N = 0
    for i in range(n):
        if vs[i] == x:
            N += 1
    res += combinations_count(N,r)
print(res)