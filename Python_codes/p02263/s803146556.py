form = input().split()
s = []
for c in form:
    if c in "+-*":
        s.append(str(eval( "{2} {0} {1}".format(c,s.pop(),s.pop()) )))
    else:
        s.append(c)
print(s[0])