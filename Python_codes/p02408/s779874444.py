A = [[i for i in range(1 ,14)] for j in range(4)]
a = int(input())
for i in range(a):
    b,c = map(str,input().split())
    c=int(c)
    if b=="S":
        A[0].remove(c)
    if b=="H":
        A[1].remove(c)
    if b=="C":
        A[2].remove(c)
    if b=="D":
        A[3].remove(c)
def name(number,name):
    if A[number]==[]:
        pass
    else:    
        x=A[number]
        x=map(str,x)
        print("%s " %name+("\n%s " %name).join(x))
    
name(0,"S")
name(1,"H")
name(2,"C")
name(3,"D")