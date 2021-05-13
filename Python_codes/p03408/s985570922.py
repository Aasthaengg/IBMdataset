n = int(input())
s = []

for a in range(n):
    s.append(input())

t = []
m = int(input())

for a in range(m):
    t.append(input())

kind = list(set(s))
kind_length = len(kind)

counter = dict()
for a in range(kind_length):
    counter[kind[a]] = 0

for a in range(n):
    counter[s[a]] += 1

for a in range(m):
    if t[a] not in counter:
        continue
    counter[t[a]] -= 1

print(max(max(counter.values()), 0))
