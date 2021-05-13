h, n = map(int, input().split())
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))
inf = 1001001001
lis = [inf] * (2*10**4+5)
lis[0] = 0
for i in range(len(lis)):
    for j in range(n):
        a = ab[j][0]
        b = ab[j][1]
        if i+a < len(lis):
            lis[i+a] = min(lis[i]+b, lis[i+a])
print(min(lis[h:]))