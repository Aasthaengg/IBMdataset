import bisect
n = int(input())
a = sorted(map(int, input().split()))

ai = a[-1]
half_ai = ai // 2

i_left = bisect.bisect_left(a, half_ai)
i_right = bisect.bisect_right(a, half_ai)
if (a[i_left] == half_ai):
    print(ai, half_ai)
    exit()

if (i_left == i_right and i_left == 0):
    print(ai, a[0])
    exit()

if (abs(half_ai - a[i_left - 1]) >=
        abs(half_ai - a[i_right]) and i_right != len(a) - 1):
    print(ai, a[i_right])
else:
    print(ai, a[i_left - 1])
