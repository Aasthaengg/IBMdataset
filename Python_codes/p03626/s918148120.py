n = int(input())
s = input()
mod = 1000000007

if n == 1:
    ans = 3
else:
    i = 1
    if s[0] == s[1]:
        ans = 6
        c = 2
        i += 1
    else:
        c = 1
        ans = 3

    while i < n-1:
        if c == 1:
            if s[i] == s[i+1]:
                c = 2
                i += 1
                ans *= 2
                ans %= mod
            else:
                c = 1
                ans *= 2
                ans %= mod
        elif c == 2:
            if s[i] == s[i+1]:
                c = 2
                i += 1
                ans *= 3
                ans %= mod
            else:
                c = 1
        else:
            if s[i] == s[i+1]:
                c = 2
                i += 1
            else:
                c = 1
        i += 1
    if s[-1] != s[-2]:
        if n >= 3:
            if s[-2] != s[-3]:
                ans *= 2
                ans %= mod
        else:
            ans *= 2
            ans %= mod
print(ans%mod)