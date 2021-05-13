n = int(input())
l0 = 2
l1 = 1
L = 0
if n == 1:
    print(l1)
    exit()
else:
    for i in range(2, n+1):
        L = l0 + l1
        l0 = l1
        l1 = L
print(L)