(a, b, x) = map(int, input().split())

n_lt_a = a // x + 1
n_lt_b = b // x + 1

if a % x == 0:
    ans = n_lt_b - n_lt_a + 1
else:
    ans = n_lt_b - n_lt_a
print(ans)
