s=input()
S=s.split()
a=0
b=0
c=0
a=int(S[0])+int(S[1])
b=int(S[0])-int(S[1])
c=int(S[0])*int(S[1])
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
elif c>=a and c>=b:
    print(c)