n, p = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] %= 2
cnt_zero = a.count(0)
cnt_one = n - cnt_zero
ans = 0
def nCk(n, k):
    if k > n - k:
        return nCk(n, n - k)
    ret = 1
    for i in range(k):
        ret *= n - i
    for i in range(k):
        ret //= i + 1
    return ret
ans = 0
c = 0
for i in range(p, cnt_one + 1, 2):
    c += nCk(cnt_one, i)
ans = (2 ** cnt_zero) * c
print(ans)