
n = int(input())

dif_max = - 10 ** 10
min_v = 10 ** 10

for i in range(n):
    r = int(input())
    dif_max = max(dif_max, r - min_v)
    min_v = min(min_v, r)

print(dif_max)