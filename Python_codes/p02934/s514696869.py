n = int(input())
a = list(map(int, input().split()))
b = 1
for i in range(n):
    b = b * a[i]
c = 0
for j in range(n):
    c += (b / a[j])
print(b / c)