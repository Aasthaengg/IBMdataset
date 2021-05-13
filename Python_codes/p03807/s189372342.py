n, *a_l = map(int, open(0).read().split())
odd = 0
for a in a_l:
    if a%2 == 1:
        odd += 1
if odd %2 == 0:
    print('YES')
else:
    print('NO')