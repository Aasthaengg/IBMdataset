# stack
exp = input().split()
s = []

for lt in exp:
    if lt == '+' or lt == '-' or lt == '*':
        rhs = s.pop()
        lhs = s.pop()
        if lt == '+':
            s.append(lhs + rhs)
        if lt == '*':
            s.append(lhs * rhs)
        if lt == '-':
            s.append(lhs - rhs)
    else:
        s.append(int(lt))
        
print(str(s[0]))