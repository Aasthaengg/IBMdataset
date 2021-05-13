# stack
exp = [i for i in input().split()]
s = []

for lt in exp:
    if lt == '+':
        rhs = s.pop()
        lhs = s.pop()
        s.append(lhs + rhs)
    elif lt == '*':
        rhs = s.pop()
        lhs = s.pop()
        s.append(lhs * rhs)
    elif lt == '-':
        rhs = s.pop()
        lhs = s.pop()
        s.append(lhs - rhs)
    else:
        s.append(int(lt))
        
print(str(s[0]))