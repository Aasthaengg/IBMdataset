n = int(input())
a = list(map(int, input().split()))

l1 = 0
l2 = sum(a)
d = l2
for i in range(n):
    l1 += a[i]
    d = min(d, abs(2*l1 - l2))
print(d)