s = input()

res = 0
for i in range(2**(len(s)-1)):
    pos = 0
    for j in range(len(s)-1):
        if (i >> j) & 1:
            res += int(s[pos:j+1])
            pos = j + 1
    res += int(s[pos:])

print(res)