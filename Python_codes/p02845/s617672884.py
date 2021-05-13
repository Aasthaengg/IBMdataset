n = int(input())
a = list(map(int, input().split()))

m = 10**9+7
r, b, g = 0, 0, 0
ans = 1

for aa in a:
    if aa == r == b == g:
        ans *= 3
    elif aa == r == b or aa == b == g or aa == g == r:
        ans *= 2
    elif aa != r and aa != b and aa != g:
        print(0)
        exit()
    ans %= m

    aa += 1
    if aa > r:
        r = aa
    elif aa > b:
        b = aa
    elif aa > g:
        g = aa

print(ans%m)