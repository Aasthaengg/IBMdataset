n = int(input())
x = list(map(int, input().split()))
t = sorted(x)
m = t[n // 2]
p = t[n // 2 - 1]
for y in x:
    if y >= m:
        print(p)
    else:
        print(m)
