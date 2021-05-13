L,R,d=map(int,input().split())
i=L//d
if L%d==0:
    i-=1
j=R//d
print(j-i)