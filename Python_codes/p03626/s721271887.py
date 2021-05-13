n = int(input())
s1 = input()
s2 = input()
mod = 10**9 + 7
ans = -1
for i, c in enumerate(s1):
    if i==0:
        if s1[i]==s2[i]:
            ans = 3
        else:
            ans = 6
    else:
        if s1[i-1]==s1[i] and s2[i-1]==s2[i]:
            continue
        elif s1[i-1]==s2[i-1] and s1[i]==s2[i]:
            ans *= 2
        elif s1[i-1]==s2[i-1] and s1[i]!=s2[i]:
            ans *= 2
        elif s1[i-1]!=s2[i-1] and s1[i]==s2[i]:
            ans *= 1
        else:
            ans *= 3
        ans %= mod
print(ans%mod)