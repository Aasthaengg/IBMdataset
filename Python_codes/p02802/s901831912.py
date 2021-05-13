n, m = map(int, input().split())

ac = 0
wa = 0
acs = [0] * n
was = [0] * n
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == 'AC':
        if not acs[p]:
            ac += 1
            wa += was[p]
            acs[p] += 1
    else:
        if not acs[p]:
            was[p] += 1
print(ac, wa)
