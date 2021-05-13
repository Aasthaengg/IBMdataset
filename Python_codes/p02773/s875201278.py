import collections
N = int(input())
ls = []
for i in range(N):
    ls.append(input())

count = collections.Counter(ls)
maxval = max(count.values())
K = [k for k, v in count.items() if v == maxval]
L = sorted(K)
for i in L:
    print(i)