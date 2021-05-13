A,B=map(int,input().split())
a=A
b=A
c=0
while b<B:
    b+=(-1)+a
    c+=1
if B>=2:
    print(c+1)
if B==1:
    print(0)