n, m = map(int, input().split())
d = [0] * m

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(a[0]):
        d[a[j+1]-1] += 1

c = 0
for num in d:
    if num == n:
        c += 1
print(c)