a=list(input())
b=list(input())
c=list(input())
a.reverse()
b.reverse()
c.reverse()
p="a"
while True:
    if p=="a":
        if len(a)==False:
            print("A")
            break
        p=a.pop()
    elif p=="b":
        if len(b)==False:
            print("B")
            break
        p=b.pop()
    elif p=="c":
        if len(c)==False:
            print("C")
            break
        p=c.pop()