n, l = map(int, input().split())
a =  [l + i for i in range(n)]

a.sort(key=lambda x: abs(x))
del a[0]

print(sum(a))