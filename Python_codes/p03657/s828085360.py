a, b = [int(x) for x in input().split()]

print("Possible" if ((a + b) % 3) * (a % 3) * (b % 3) == 0 else "Impossible")
