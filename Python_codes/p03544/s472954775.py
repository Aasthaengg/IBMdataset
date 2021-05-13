n = int(input())
l0 = 2
l1 = 1
l = 0
if n == 1:
    print(l1)
else:
    for i in range(2, n + 1):
        l = l1 + l0
        l0 = l1
        l1 = l
    print(l)