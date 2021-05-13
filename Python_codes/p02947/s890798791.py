N = int(input())
l = []
c=0
for i in range(N):
    l.append(sorted(input()))
l.sort()

base =0
next = 1
ren = 1
while True:
    if l[base] == l[next]:
        ren += 1
        next += 1
    else:
        c += ren * (ren - 1) // 2
        base = next
        next += 1
        ren = 1
    if next == N:
        c += ren * (ren-1) // 2
        break
print(c)
