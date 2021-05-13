C1=input()
C2=input()
C1new="".join(list(reversed(C1)))
C2new="".join(list(reversed(C2)))
if (C1==C2new)&(C2==C1new):
    print("YES")
else:
    print("NO")