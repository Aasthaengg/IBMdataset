
n = int(input())
v = list(map(int, input().split()))

kisu = [0]*(10**6)
gusu = [0]*(10**6)
for i in range(n):
    if i % 2 == 0:
        gusu[v[i]] += 1
    else:
        kisu[v[i]] += 1

count = 0
gusu_m = gusu.index(max(gusu))
kisu_m = kisu.index(max(kisu))

if gusu_m == kisu_m:

    gusu[gusu_m] = 0
    kisu[kisu_m] = 0
    if max(gusu) > max(kisu):
        gusu_m = gusu.index(max(gusu))
    else:
        kisu_m = kisu.index(max(kisu))

for i in range(n):
    if i % 2 == 0 and gusu_m != v[i]:
        count += 1
    if i % 2 != 0 and kisu_m != v[i]:
        count += 1

print(count)
