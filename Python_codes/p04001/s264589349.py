s=input()
l=len(s)-1
res = 0

for i in range(2**l):
    s_new = s[0]
    for j, c in enumerate(s[1:]):
        flag = True if (i>>j)%2==1 else False
        s_new += c if flag else "+"+c
    res += eval(s_new)
print(res)
