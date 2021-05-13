a = list(map(int, input().split()))
count_a = 0
count_b = 0
count_c = 0
count_d = 0

for i in range(4):
    if a[i] == 1:
        count_a += 1
    if a[i] == 4:
        count_b += 1
    if a[i] == 7:
        count_c += 1
    if a[i] == 9:
        count_d += 1

if count_a == 1 and count_b == 1 and count_c == 1 and count_d == 1:
    print('YES')
else:
    print('NO')
