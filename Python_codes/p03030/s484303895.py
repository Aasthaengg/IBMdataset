n = int(input())

a = []
for i in range(n):
    s, p = input().split()
    a.append((s, -int(p), i + 1))
a.sort()
for b in a:
    print(b[2])
