from collections import defaultdict
n,t = map(int,input().split())
a = [int(i) for i in input().split()]
dct = defaultdict(int)
mv = mk = 0
for i in range(n)[::-1]:
    k = mv-a[i]
    if k > 0: dct[k] += 1
    mk = max(mk,k)
    mv = max(mv,a[i])
print(dct[mk])