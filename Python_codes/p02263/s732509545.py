import re
pat = re.compile(r'(\-?\d+\.?\d*)\s(\-?\d+\.?\d*)\s([\+\-\*/])(?!\d)')

def revPolish(f):
    global pat
    f = pat.sub(lambda m: str(eval(m.group(1) + m.group(3) + m.group(2))),f)
    if f[-1] in '+-*/':
        return revPolish(f)
    else:
        return f

print(revPolish(input()))
