n, m = [int(x) for x in input().split()]
f_set = set()
t_set = set()
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    if a == 1:
        f_set.add(b)
    elif b == n:
        t_set.add(a)
print("POSSIBLE" if len(f_set & t_set) >= 1 else "IMPOSSIBLE")