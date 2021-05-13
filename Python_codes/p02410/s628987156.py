n = list(map(int, input().split()))
a = []
b = []

for i in range(n[0]):
    a.append(list(map(int, input().split())))

for i in range(n[1]):
    b.append(int(input()))

for i in range(n[0]):
    ab_sum = 0
    for j in range(n[1]):
        ab_sum += a[i][j] * b[j]
    print(ab_sum)

