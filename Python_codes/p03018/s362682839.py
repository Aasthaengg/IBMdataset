s = list(input())
n = len(s)
ans = 0
c = 0
i = 0
while i < n-1:
    if s[i] == "B" and s[i+1] == "C":
        ans += c
        i += 1
    elif s[i] == "A":
        c += 1
    else:
        c = 0
    i += 1
print(ans)