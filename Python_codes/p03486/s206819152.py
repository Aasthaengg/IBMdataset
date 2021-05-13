
s=list(input())
t=list(input())
s=sorted(s)
t=sorted(t)
x=s[0]
for i in range(len(s)-1):
    x=x+s[i+1]
y=t[-1]
for i in range(len(t)-1):
    y=y+t[-i-2]




l=[]
l.append(x)
l.append(y)
l=sorted(l)

if l.index(x)<l.index(y):
    print("Yes")
else:
    print("No")
