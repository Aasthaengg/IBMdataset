n, p = map(int, input().split())
a = list(map(int, input().split()))

length = len(a)
even = len([i for i in a if i % 2 == 0])
odd = len([i for i in a if i % 2 == 1])

if length == even and p == 1:
    print(0)
elif length == even:
    print(2 ** n)
else:
    print(2 ** n // 2)