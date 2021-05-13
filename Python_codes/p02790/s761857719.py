a, b = [int(s) for s in input().split()]
print(sorted([str(a)*b, str(b)*a])[0])
