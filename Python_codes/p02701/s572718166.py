n = int(input())
s = []
for _ in range(n):
    s.append(input())

types = set(s)
print(len(types))