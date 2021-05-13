r, c = input().split()
r = int(r)
c = int(c)

a = [0]*r

for i in range(r):
    a[i] = list(map(int, input().split()))
    a[i].append(sum(a[i]))
    print(*a[i])
print(*list(map(sum, zip(*a))))