s=input()
r=s.split()
x=int(r[0])
y=int(r[1])
r=x%y

while r!=0:
    x=y
    y=r
    r=x%y

print(y)
