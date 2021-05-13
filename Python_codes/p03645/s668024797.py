n, m = input().split()
a, b = set(), set()
for _ in range(int(m)):
    r = set(input().split())
    if "1" in r:
        a |= r
    if n in r:
        b |= r
print("POSSIBLE" * len(a & b) or "IMPOSSIBLE")
