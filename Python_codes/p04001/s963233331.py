s = input()
ans = 0
for i in range(2**(len(s)-1)):
    plus = [""]*(len(s))
    fomula = ""
    for j in range(len(s)-1):
        if(i >> j & 1):
            plus[j] = "+"
    for k in range(len(s)):
        fomula += s[k] + plus[k]
    ans += eval(fomula)
print(ans)