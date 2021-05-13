n = int(input())
a = [int(i) for i in input().split()]
t = 1
for i in a:
    if i % 2 == 0: t *= 2
print(3 ** n - t)