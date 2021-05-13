from collections import Counter
n = int(input())
a = list(map(int,input().split()))

c = Counter(a)
#print(c)

s = 0
for i in c.values():
    s += i * (i-1) // 2

for i in range(n):
    print(s - c[a[i]] + 1)