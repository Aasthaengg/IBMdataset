n = int(input())
a = [int(x) for x in input().split()]
a.sort()

d = 0
for i in range(1, n):
   d += a[i] - a[i-1]
print(d)
