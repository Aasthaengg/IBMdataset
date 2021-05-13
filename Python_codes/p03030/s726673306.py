from operator import itemgetter

n = int(input())
a = []
for i in range(n):
    s, p = input().split()
    a.append((i + 1, s, -int(p)))
a.sort(key=itemgetter(1, 2))
for i, _, _ in a:
    print(i)
