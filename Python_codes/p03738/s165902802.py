def solve(i, j):
    if i > j:
        print("GREATER")
        exit()
    if i < j:
        print("LESS")
        exit()
a = input()
b = input()
solve(len(a), len(b))
if int(a) == int(b):
    print("EQUAL")
    exit()
for ai, bi in zip(a, b):
    solve(int(ai), int(bi))