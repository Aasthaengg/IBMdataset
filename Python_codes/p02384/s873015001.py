
def dice():
    import random as ran

    dnum = list(map(int,input().split()))
    q = int(input())
    up = dnum[0]
    un = dnum[5]
    ri = dnum[2]
    le = dnum[3]
    fr = dnum[1]
    ba = dnum[4]
    tmp = int(0)
    tmp2 = int(0)
    order = ["S","N","E","W"]

    for i in range(q):
        qup,qfr = (int(x) for x in input().split())
        while True :
            x = ran.choice(order)
            if (x == "S"):
                tmp = fr
                tmp2 = un
                fr = up
                up = ba
                un = tmp
                ba = tmp2

            elif (x == "N"):
                tmp = un
                tmp2 = up
                up = fr
                un = ba
                fr = tmp
                ba = tmp2

            elif (x == "E"):
                tmp = up
                tmp2 = un
                up = le
                un = ri
                ri = tmp
                le = tmp2

            elif (x == "W"):
                tmp = un
                tmp2 = up
                up = ri
                un = le
                ri = tmp
                le = tmp2

            if (up == qup and fr == qfr):
                print(ri)
                break
dice()

