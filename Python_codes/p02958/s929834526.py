n = int(input())
p = list(map(int, input().split()))
l = []
for i in range(n):
    p[i] -= 1
    if p[i] != i:
        l.append([i, p[i]])
if len(l) == 0:
    print('YES')
elif len(l) == 2 and l[0][1] == l[1][0] and l[0][0] == l[1][1]:
    print('YES')
else:
    print('NO')