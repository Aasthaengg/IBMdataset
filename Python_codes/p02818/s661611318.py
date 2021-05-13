# coding: utf-8

a, b, k = list(map(int, input().split(" ")))

if a <= k:
    a_after = 0
    k_after = k - a
    b_after = b - k_after if b >= k_after else 0
else:
    a_after = a - k
    b_after = b

print("{} {}".format(a_after, b_after))
