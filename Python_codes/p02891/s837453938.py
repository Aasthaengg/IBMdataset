s = input(); k = int(input())
a = 0
def count(t):
    i = 1; x = 0
    while i < len(t):
        if t[i-1] == t[i]:
            x += 1
            i += 1
        i += 1
    return x
for i in range(len(s)-1):
    if s[i] != s[i+1]: break
else: a = 1
if a == 1: print(len(s)*k//2)
else:
    if k == 1: print(count(s))
    else:
        ss = s+s; sss = ss+s
        print(count(ss)+(count(sss)-count(ss))*(k-2))