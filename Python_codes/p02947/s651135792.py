import collections

n = int(input())
l = []

for _ in range(n):
    a = sorted(input())
    l.append("".join(a))
    
ls = collections.Counter(l)
r = list(ls.values())

def cul(n):
    return n*(n-1)/2

ans = 0
for i in r:
    ans += cul(i)
print(int(ans))