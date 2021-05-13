n,m = map(int,input().split())
a = list(map(int,input().split()))

s = [0]
for i in range(n):
    s.append((s[i]+a[i])%m)

from collections import Counter
d = Counter(s)

temp = 0
for i in d.values():
    temp+=i*(i-1)//2

print(temp)