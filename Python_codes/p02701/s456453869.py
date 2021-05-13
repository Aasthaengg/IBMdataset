from collections import Counter

l = []

N = int(input())

for i in range(N):
    l.append(input())

c = Counter(l)
print(len(c))
