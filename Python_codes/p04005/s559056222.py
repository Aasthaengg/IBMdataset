a,b,c=map(int,input().split())

def block(a,b,c):
    blocksum=a*b*c
    if a%2==0 or b%2==0 or c%2==0:
        print(0)
        return
    else:
        al=[]
        al.append(a*b)
        al.append(b*c)
        al.append(a*c)
        al=sorted(al)
        print(al[0])
block(a,b,c)