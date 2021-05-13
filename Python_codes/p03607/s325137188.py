import collections as cl
N = int(input())
x = []
count = 0

for i in range(N):
    a = int(input())
    x.append(a)

d = cl.Counter(x)

for i in d.values():
    if i % 2 == 1:
        count += 1
print(count)
