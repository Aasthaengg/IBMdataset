n, a, b = [int(i) for i in input().split()]
k = abs(a-b-1)
if k%2 == 0:
    print("Borys")
else:
    print("Alice")