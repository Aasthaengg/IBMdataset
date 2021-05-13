s = list(input())
i = len(s)
p = 0
while i >= 3:
    if s[i-1] == s[i-2]:
        i -= 3
        p += 2
    else:
        i -= 1
        p += 1

if i <= 1:
    print(p+i)
else:
    if s[i-1] == s[i-2]:
        print(p+1)
    else:
        print(p+2)