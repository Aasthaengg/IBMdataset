sa=list(input())
sb=list(input())
sc=list(input())
sa.append("x")
sb.append("x")
sc.append("x")
l=[sa,sb,sc]
na=len(sa)-1
nb=len(sb)-1
nc=len(sc)-1
a=0
b=0
c=0
f=0
turn="a"
while f==0:
    if turn=="a":
        a+=1
        turn=l[0][a-1]
        
    elif turn=="b":
        b+=1
        turn=l[1][b-1]
    else:
        c+=1
        turn=l[2][c-1]
    if a==na+1:
        print("A")
        exit()
    elif b==nb+1:
        print("B")
        exit()
    elif c==nc+1:
        print("C")
        exit()
    
    
