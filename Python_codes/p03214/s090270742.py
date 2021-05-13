n = int(input())
a = list(map(int,input().split()))
b = sum(a) / n
c = abs(a[0] - b)
d = 0

for i in range(1,n):
    if abs(a[i] - b) < c:
        c = abs(a[i] - b)
        d = i

print(d)