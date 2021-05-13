n = int(input())
s = input()
S = input()
ans = 3
i = 0
if s[i] == S[i]:
    ans *= 1
    i += 1
else:
    ans *= 2
    i += 2
while i < n:
    if s[i] == S[i]:
        if s[i-1] == S[i-1]:ans *= 2;i += 1
        else:ans *= 1;i += 1
    else:
        if s[i-1] == S[i-1]:ans *= 2;i += 2
        else:ans *= 3;i += 2
print(ans % (10**9+7))