a,b,c=map(int,input().split())

def number(a,b,c):
    num=a%b
    sumn=0
    for i in range(2,10000000):
        if sumn==c:
            print("YES")
            return
        sumn+=num
        if sumn>b:
            sumn=sumn%b
    print("NO")
number(a,b,c)