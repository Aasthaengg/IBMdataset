n, m = map(int, input().split())
if m & 1:
    if n & 1:
        left_1 = 1
        right_1 = n // 2
        left_2 = (n // 2) + 1
        right_2 = n
    else:
        left_1 = 1
        right_1 = n // 2 - 1
        left_2 = (n // 2) + 1
        right_2 = n
else:
    if n & 1:
        left_1 = 1
        right_1 = n // 2
        left_2 = (n // 2) + 1
        right_2 = n
    else:
        left_1 = 1
        right_1 = n // 2 - 1
        left_2 = (n // 2) + 1
        right_2 = n
for _ in range(m // 2):
    print(left_1, right_1)
    left_1 += 1
    right_1 -= 1
for _ in range(m // 2, m):
    print(left_2, right_2)
    left_2 += 1
    right_2 -= 1
