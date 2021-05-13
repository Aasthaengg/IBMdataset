n = int(input())
a = list(map(int, input().split()))
a.sort()
ai = a[-1]
aj = a[0]
center = ai // 2
diff = 10**10

for i in range(n-1):
    if abs(center - a[i]) <= diff and aj < a[i]:
        diff = abs(center - a[i])
        aj = a[i]

print(str(ai) + " " + str(aj))