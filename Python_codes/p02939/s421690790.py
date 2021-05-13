s = input()
i = 1; a = 1; n = 1
while i < len(s):
    if a == 1 and s[i-1] == s[i]:
        a = 2; i += 2; n += 1
    else:
        if i == len(s)-2 and s[i] == s[i+1]: n -= 1
        a = 1; i += 1; n += 1
print(n)