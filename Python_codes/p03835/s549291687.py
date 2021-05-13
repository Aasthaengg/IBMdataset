k, s = map(int, input().split())
def two_sum(k, s):
    if s < 0:
        return 0
    elif k >= s:
        return s + 1
    elif s//2 > k:
        return 0
    else:
        return s + 1 - 2 * (s - k)

ans = 0
for x in range(k+1):
    ans += two_sum(k, s - x)
print(ans)