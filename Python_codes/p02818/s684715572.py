a, b, k = list(map(int, input().rstrip().split()))
if a > k:
    a -= k
    k = 0
else:
    # a <= k
    k -= a
    a = 0

if b > k:
    b -= k
else:
    # b <= k
    b = 0


print('{} {}'.format(a, b))

