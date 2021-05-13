import re

def dfs(i, formula_str):
    if i == 4:
        res = int(formula_str[0])
        for j in range(2, 7, 2):
            if formula_str[j-1] == "+":
                res += int(formula_str[j])
            else:
                res -= int(formula_str[j])
        if res == 7:
            return True, formula_str
        return False, formula_str
    else:
        f_1, formula_str_1 = dfs(i+1, formula_str + "+" + s[i])
        f_2, formula_str_2 = dfs(i+1, formula_str + "-" + s[i])
        if f_1:
            return True, formula_str_1
        elif f_2:
            return True, formula_str_2
        else:
            return False, None

s = input()
f, ans = dfs(1, s[0])
print(ans + "=7")
