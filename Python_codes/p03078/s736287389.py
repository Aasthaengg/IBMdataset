x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
l = []
for i in a:
    for j in b:
        l.append(i + j)
c.sort(reverse=True)
l.sort(reverse=True)
l = l[:k]
l2 = []
for i in c:
    for j in l:
        l2.append(i + j)
l2.sort(reverse=True)
print(*l2[:k], sep="\n")
