MOD = 1000000007

n = int(input())
s1 = input()
s2 = input()

if s1[0] == s2[0]:
    ans = 3
    i = 1
    prev = 1
else:
    ans = 6
    i = 2
    prev = 2

while i<n:
    
    if s1[i] == s2[i]:
        i += 1
        if prev == 1:
            ans *= 2
        else:
            prev = 1
    else:
        i += 2
        if prev == 1:
            ans *= 2
            prev = 2
        else:
            ans *= 3
    ans %= MOD

print(ans)