n = int(input())
s1 = input()
s2 = input()
ans = 0
mod = 10**9+7

if s1[0] != s2[0]:
    ans = 6
    i = 2
    b = 1
else:
    ans = 3
    i = 1
    b = 0

while i < n:
    if s1[i] != s2[i]:
        i += 2
        if b:
            ans = ans*3%mod
        else:
            ans = ans*2%mod
            b = 1
    else:
        i += 1
        if b:
            b = 0
        else:
            ans = ans*2%mod
print(ans)
