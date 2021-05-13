from operator import itemgetter

n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]

ab.sort()
ab.sort(key=itemgetter(1))
t = 0
for a, b in ab:
    t += a
    if t > b:
        print('No')
        break
else:
    print('Yes')
