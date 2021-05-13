n = int(input())
s1 = input()
s2 = input()
mod = 10 ** 9 + 7

com = 1
pre = "e"
flag = True
for i in range(n):
    if s1[i] == s2[i]:
        if pre == "e":
            com *= 3
        elif pre == "v":
            com *= 2
            com %= mod
        else:
            pass
        pre = "v"
    else:
        if flag == True:
            if pre == "e":
                com *= 6
            elif pre == "v":
                com *= 2
                com %= mod
            else:
                com *= 3
                com %= mod
            flag = False
        else:
            flag = True
        pre = "h"
print(com)