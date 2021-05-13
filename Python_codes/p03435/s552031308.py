c11,c12,c13=map(int,input().split())
c21,c22,c23=map(int,input().split())
c31,c32,c33=map(int,input().split())
f=0
if not c11-c12==c21-c22==c31-c32:
    f=1
if not c11-c13==c21-c23==c31-c33:
    f=1
if not c12-c13==c22-c23==c32-c33:
    f=1
if not c11-c21==c12-c22==c13-c23:
    f=1
if not c11-c31==c12-c32==c13-c33:
    f=1
if not c21-c31==c22-c32==c23-c33:
    f=1
print("Yes" if f==0 else "No")
