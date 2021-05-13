a, b, c = [int(s) for s in input().split()]

print(["NO", "YES"][a - b == b - c])