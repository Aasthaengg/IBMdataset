n = int(input())
x = list(map(int, input().split()))

l = sorted(x)

m1 = l[n // 2 - 1]
m2 = l[n // 2]

for y in x:
    if y <= m1:
        print(m2)
    else:
        print(m1)
