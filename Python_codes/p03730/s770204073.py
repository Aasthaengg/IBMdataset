A, B, C = map(int, input().split())
calc = 0

for i in range(1000):
    calc += A
    rem = calc % B
    if rem == C:
        print('YES')
        exit()

print('NO')
