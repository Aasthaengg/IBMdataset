s = input()

A = 0
B = 0
C = 0

for x in s:
    if x == 'a':
        A += 1
    elif x == 'b':
        B += 1
    else:
        C += 1

l = sorted([A, B, C])

print('YES' if (l[2] <= l[1] + 1 and l[0] == l[1]) or (l[2] == l[1] and l[0] == l[1] - 1) else 'NO')
