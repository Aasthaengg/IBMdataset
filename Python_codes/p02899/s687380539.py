n = int(input())
a = list(map(int, input().split()))
arriv = {}
l = []

for i in range(1, n + 1):
    arriv[i] = a[i - 1]

arriv_2 = sorted(arriv.items(), key = lambda x:x[1])

for i in range(n):
    l.append(str(arriv_2[i][0]))

print(' '.join(l))
