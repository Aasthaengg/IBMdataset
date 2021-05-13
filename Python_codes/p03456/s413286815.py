a, b = input().split()
L = list(map(lambda x : x * x, range(400)))
c = int(a + b)
if c in L:
    print("Yes")
else:
    print("No")