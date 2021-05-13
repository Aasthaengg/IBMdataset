a, b, k = [int(x) for x in input().split()]
if a + k - 1 < b - k + 1:
    l = list(range(a, a + k)) + list(range(b - k + 1, b + 1))
else:
    l = list(range(a, b + 1))
for ans in l:
    print(ans)
