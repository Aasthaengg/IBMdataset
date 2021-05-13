n = int(input())
a, b = map(int, input().split())
p = list(int(x) for x in input().split())
k1, k2, k3 = 0, 0, 0
for i in range(n):
    if p[i] <= a:
        k1 += 1
    elif p[i] <= b:
        k2 += 1
    else:
        k3 += 1
print(min([k1, k2, k3]))