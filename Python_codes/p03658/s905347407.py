n, k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
c = 0
for i in range(k):
    c += a[i]
print(c)