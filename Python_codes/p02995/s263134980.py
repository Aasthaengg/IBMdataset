A,B,C,D =map(int,input().split())
x = C
y = D
while y>0:
    x,y = y,x%y
E = (C//x)*D
bc = B//C
bd = B//D
be = B//E
b = B-(bc+bd-be)
ac = (A-1)//C
ad = (A-1)//D
ae = (A-1)//E
a = A-1-(ac+ad-ae)
print(b-a)