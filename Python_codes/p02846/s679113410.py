from math import floor

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

diff1 = (a1 - b1) * t1
diff2 = (a2 - b2) * t2
diff = diff1 + diff2

if diff1 * diff > 0:
    print("0")

elif diff == 0:
    print("infinity")

else:
    diff1 = abs(diff1)
    diff2 = abs(diff2)
    n = diff2 / (diff2 - diff1)

    if n == floor(n):
        n = floor(n)
        ans = 2 * n - 2
    else:
        n = floor(n)
        ans = 2 * n - 1

    print(ans)

