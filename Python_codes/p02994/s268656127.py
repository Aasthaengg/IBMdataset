n, l = map(int, input().split())
a = []
b = []
for i in range(1,n+1):
    a.append(l+i-1)
    b.append(abs(l+i-1))
x = b.index(min(b))
print(sum(a)-a[x])
