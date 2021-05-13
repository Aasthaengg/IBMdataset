n = int(input())

l0 = 2
l1 = 1
if n == 1:
    print(l1)
else:
    for i in range(1, n):
        l2 = l0 + l1
        l0 = l1
        l1 = l2
    print(l2)