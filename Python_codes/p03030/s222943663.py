n = int(input())
r = []
for i in range(n):
    s, p = input().split()
    r.append((i + 1, s, int(p)))
r.sort(key=lambda x: x[2], reverse=True)
r.sort(key=lambda x: x[1])
for ri in r:
    print(ri[0])