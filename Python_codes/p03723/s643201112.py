A, B, C = list(map(int, input().split()))

if A == B == C:
    if A % 2 == 0:
        print('-1')
    else:
        print('0')
else:
    count = 0
    for _ in range(10 ** 9):
        if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
            print(count)
            break
        tmp_A = A
        tmp_B = B
        tmp_C = C
        A = (tmp_B + tmp_C) / 2
        B = (tmp_A + tmp_C) / 2
        C = (tmp_B + tmp_A) / 2
        count += 1
