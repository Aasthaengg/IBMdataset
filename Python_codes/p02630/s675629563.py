import collections
n = int(input())
a = list(map(int,input().split()))
q = int(input())
l = [list(map(int,input().split())) for i in range(q)]
b,c = [list(i) for i in zip(*l)]
x = collections.Counter(a)
y = sum(a)
for i in range(q):
    if b[i] in x:
        y -= x[b[i]] * b[i]
        y += x[b[i]] * c[i]
        x[c[i]] += x[b[i]]
        x[b[i]] = 0
    print(y)