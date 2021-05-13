s = input()
l = len(s)

for i in range(2**(l-1)):
    ans = 0
    a = s[0]
    for j in range(l-1):
        if i >> j & 1 == 0:
            a += '+' + s[j+1]
        elif i >> j & 1 == 1:
            a += '-' + s[j+1]
    ans = eval(a)
    if ans == 7:
        print(a + '=7')
        exit()