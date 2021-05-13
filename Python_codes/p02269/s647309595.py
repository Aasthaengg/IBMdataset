n = int(input())
d = {}
for i in range(n):
    x = input()
    if x[0] == "i":
        d[x[7:]] = 1
    else :
        if(x[5:] in d.keys()) : print("yes")
        else : print("no")
