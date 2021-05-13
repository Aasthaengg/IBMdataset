n = int(input())

l2 = 1
l1 = 2

if n == 0:
    l2 = l1
elif n == 1:
    pass
else:
    for i in range(n-1):
        l0 = l1
        l1 = l2
        l2 = l1 + l0

print(l2)