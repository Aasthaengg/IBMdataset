a,b=map(int, input().split(" "))
wh="."
bl="#"
print(100,100)
for i in range(100):
    out=""
    if i%2==0:
        for k in range(50):
            out+=bl
        for k in range(50):
            out+=wh
    else:
        for i in range(25):
            if a > 1:
                out+=wh
                a-=1
            else:
                out+=bl
            out+=bl

        for i in range (25):
            out+=wh
            if b > 1:
                out+=bl
                b-=1
            else:
                out+=wh

    print(out)
