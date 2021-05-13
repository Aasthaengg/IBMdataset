#coding:utf-8
def kisuu(a):
    b = []
    for i in range(a):
        if i%2==0:
            b.append("#")
        else:
            b.append(".")
    return(b)

def gusuu(a):
    b = []
    for i in range(a):
        if i%2==0:
            b.append(".")
        else:
            b.append("#")
    return(b)
h = 1
w = 1

while h+w != 0:
    h, w=input().rstrip().split(" ")
    h = int(h)
    w = int(w)
    if h == 0:
        if w==0:
            break

    ki = "".join(kisuu(w))
    gu = "".join(gusuu(w))

    for i in range(h):
        #?\???°
        if i%2 ==0:
            print(ki)
        else:
            print(gu)

    print("")