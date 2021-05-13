x, y, z, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ab = []
for i in range(x):
    for j in range(y):
        ab.append(a[i] + b[j])
ab.sort(reverse=True)
ab = ab[:k]
rec = []
for i in range(min(x*y, k)):
    for j in range(z):
        rec.append(ab[i] + c[j])

rec.sort(reverse=True)
rec = rec[:k]
print(*rec, sep='\n')