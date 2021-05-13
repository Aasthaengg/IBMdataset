a, b = [int(n) for n in input().split()]

if (a+b) % 2 == 0:
    print(int((a+b)/2))
else:
    print("IMPOSSIBLE")
