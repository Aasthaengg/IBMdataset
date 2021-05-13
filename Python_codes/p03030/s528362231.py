from operator import itemgetter

n = int(input())
sp = [[] for _ in range(n)]
for i in range(n):
    s, p = input().split()
    p = -int(p)
    sp[i] = [s, p, i + 1]

sp.sort(key=itemgetter(0, 1))
for i in range(n):
    print(sp[i][2])
