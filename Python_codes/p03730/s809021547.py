A, B, C = [int(x) for x in input().split()]

ok = False
for i in range(1, B):
    if i * A % B == C:
        ok = True
        break

if ok:
    print('YES')
else:
    print('NO')