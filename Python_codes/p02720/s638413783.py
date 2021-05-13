from itertools import chain

l = [[] for _ in range(11)]
l[0] = list(map(str, range(1, 10)))
for i in range(10):
    for x in l[i]:
        last = int(x[-1])
        for m in {max(0, last-1), last, min(9 ,last+1)}:
            m = str(m)
            l[i+1].append(x+m)

q = list(map(int, chain(*l)))
q.sort()
# print(len(q))
K = int(input())

print(q[K-1])