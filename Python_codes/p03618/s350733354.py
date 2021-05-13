a = input()
n = len(a)
d = {}
for i in a:
    d[i] = d.get(i,0)+1
def cov2(x):
    return x*(x-1)//2
ans = 1 + cov2(n)
for v in d.values():
    ans -= cov2(v)
print(ans)