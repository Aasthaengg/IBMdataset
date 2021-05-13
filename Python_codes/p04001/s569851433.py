s = input()
n = len(s)-1
c = 0
for i in range(2**n):
    S = s[0]
    for j in range(n):
        if (i >> j) & 1 == 1:
            S += "+" + s[j+1]
        else:
            S += s[j+1]
    c += eval(S)
print(c)    