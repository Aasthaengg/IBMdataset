n, *a = map(int, open(0).read().split())
minus_cnt = len([1 for A in a if A < 0])
ans = sum([abs(A) for A in a])
if (0 not in a) and (minus_cnt %2 != 0):
    ans -= 2 * min([abs(A) for A in a])
print(ans)