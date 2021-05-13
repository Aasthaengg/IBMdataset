s=input()
l=len(s)
c=s.count('W')
ans='W'*c+'B'*(l-c)
w=0
b=0
for i in range(l):
    if i<=c-1 and s[i]!='W':
        w+=i
    if i>=c and s[i]!='B':
        b+=i
print(b-w)