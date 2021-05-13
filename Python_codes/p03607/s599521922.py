import collections


n = int(input())
keep = []
ans = 0
for i in range(n):
    j = int(input())
    keep.append(j)

c = collections.Counter(keep)
print(len([i[0] for i in c.items() if i[1] % 2 != 0]))
