n, l = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(l+i)
    b.append(abs(l+i))
x = b.index(min(b))
print(sum(a)-a[x])