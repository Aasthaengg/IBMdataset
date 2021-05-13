n = int(input())
if n == 0:
    print(2)
elif n == 1:
    print(1)
else:
    l1 = 2
    l2 = 1
    l3 = 0
    for i in range(n-1):
        l3 = l1
        l1 = l2
        l2 += l3
    print(l2)