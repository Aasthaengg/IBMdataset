import math
A, B = map(int, input().split())

if A <= 5:
    print('0')
elif 6 <= A <= 12:
    print(math.ceil(B / 2))
else:
    print(B)
