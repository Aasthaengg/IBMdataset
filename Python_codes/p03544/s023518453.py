n = int(input())
l0, l1 = 2, 1
for i in range(n):
    l0, l1 = l1, l0+l1
print(l0)