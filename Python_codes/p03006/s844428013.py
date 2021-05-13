#%%
import collections

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

l = []
for i in range(n):
    for j in range(n):
        tmp = str(x[i]-x[j]) + ' ' + str(y[i]-y[j])
        l.append(tmp)

c = collections.Counter(l)
a = list(c.values())
#print(a)
a.sort(reverse=True)


if n == 1:
    print(1)
else:
    print(n-a[1])