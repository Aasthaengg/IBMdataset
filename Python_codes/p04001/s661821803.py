s = input()
total = 0
n = 2**(len(s)-1)
for i in range(n):
    buf = s[0]
    for j in range(len(s)-1):
        if (i>>j)&1:
            total += int(buf)
            buf = s[j+1]
        else:
            buf += s[j+1]
    total += int(buf)
print(total)