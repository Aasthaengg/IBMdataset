s = list(input())
n = len(s) - 1

wa = 0
for i in range(2**n):
    lst = [""]*n
    for j in range(n):
        if i&(1<<j):
            lst[j] = "+"
    lst_s = [0]*(len(s) + n)
    lst_s[::2] = s
    lst_s[1::2] = lst
    #print(eval("".join(lst_s)))
    wa += eval("".join(lst_s))
print(wa)