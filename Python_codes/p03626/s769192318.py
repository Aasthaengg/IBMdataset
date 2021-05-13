mod = 1000000007
n = int(input())
s1 = input()
s2 = input()

ans = 1
for i in range(n):
    if s1[i] == s2[i]:
        if i==0:
            ans *= 3
        else:
            if s1[i-1]==s2[i-1]:
                ans *= 2
            else:
                continue
    else:
        if i==0:
            ans *= 6
        else:
            if s1[i] == s1[i-1]:
                continue
            elif s1[i-1] == s2[i-1]:
                ans *=2
            else:
                ans *= 3
    ans = ans%mod
print(ans)