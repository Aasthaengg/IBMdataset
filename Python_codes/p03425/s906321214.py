n = int(input())
m = []
apple = []
r = []
cat = []
h = []

for _ in range(n):
    s = str(input())
    if s[0]=="M":
        m.append(s)
    elif s[0]=="A":
        apple.append(s)
    elif s[0]=="R":
        r.append(s)
    elif s[0]=="C":
        cat.append(s)
    elif s[0]=="H":
        h.append(s)
    else:
        pass
a = len(m)
b = len(apple)
c = len(r)
d = len(cat)
e = len(h)
print(a*b*c + a*b*d + a*b*e + b*c*d + b*c*e + c*d*e + a*c*d + a*c*e + a*d*e + b*d*e)