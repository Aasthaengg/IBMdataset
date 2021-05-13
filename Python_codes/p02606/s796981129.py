L,R,d=map(int,input().split())
a=L//d
if L%d==0:
    a-=1
b=R//d
print(b-a)