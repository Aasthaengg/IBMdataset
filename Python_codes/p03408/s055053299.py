import heapq

n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

l = list(set(s))
total = 0
for i in l:
    total = max(total, s.count(i) - t.count(i))

print(total)