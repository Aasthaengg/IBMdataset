A, B = map(int, input().split())
a_0 = int((25 * A + 1) / 2)
a_1 = int((25 * (A + 1) - 1) / 2)
b_0 = int(10 * B)
b_1 = int(10 * (B + 1) - 1)
if a_0 >= b_0 and a_0 <= b_1:
    print(a_0)
elif b_0 >= a_0 and b_0 <= a_1:
    print(b_0)
else:
    print('-1')