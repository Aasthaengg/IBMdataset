n = int(input())
w = [int(xi) for xi in input().split()]
c = [int(xi) for xi in input().split()]


sum = 0
for xi in range(n):
    if w[xi]>c[xi]:
        sum += w[xi]-c[xi]
print(sum)
