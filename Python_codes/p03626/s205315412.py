n = int(input())
s = input()
mod = 10 ** 9 + 7
if n == 1:
    print(3)
    exit()
if s[0] == s[1]:
    i = 2
    rslt = 6
    flag = True
else:
    i = 1
    rslt = 3
    flag = False
while i < n:
    if i != n-1 and s[i] == s[i + 1]:
        if flag:
            rslt = rslt * 3 % mod
        else:
            rslt = rslt * 2 % mod
        i += 2
        flag = True
    else:
        if not flag:
            rslt = rslt * 2 % mod
        i += 1
        flag = False

print(rslt)