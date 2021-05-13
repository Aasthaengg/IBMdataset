n = input()
for i in range(2**3):
    ss =""
    ss +=n[0]
    for j in range(3):
        if((i >> j )&1==True):
            ss += "+"
            ss += n[j+1]
        else:
            ss += "-"
            ss += n[j+1]
    ans = eval(ss)
    if (ans == 7):
        ss += "=7"
        print(ss)
        break