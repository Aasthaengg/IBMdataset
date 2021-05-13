s = input()
n = len(s) - 1
for i in range(1 << n):
    p_or_m = ['-'] * n
    for j in range(n):
        if i >> j & 1:
            p_or_m[n-j-1] = '+'
    
    formula = ''
    for k in range(n):
        formula += s[k] + p_or_m[k]
    formula += s[3]
    if  eval(formula) == 7:
        print(formula + '=7')
        exit()