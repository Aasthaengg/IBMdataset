from collections import deque
def A(a):
    x=a.popleft()
    return x,a
def B(b):
    x=b.popleft()
    return x,b
def C(c):
    x=c.popleft()
    return x,c
Sa=list(input())
Sb=list(input())
Sc=list(input())
a=deque(Sa)
b=deque(Sb)
c=deque(Sc)
x=a.popleft()

#print(a,b,c,x)
while True:

    if x=="a":
        if len(a)==0:
            print("A")
            exit()
        x,a=A(a)
    elif x=="b":
        if len(b)==0:
            print("B")
            exit()
        x,b=B(b)
    elif x=="c":
        if len(c)==0:
            print("C")
            exit()
        x,c=C(c)
    #print(a,b,c,x)
    
