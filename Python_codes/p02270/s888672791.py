import math

def search(cap, loads, num_tracks):
    num = 0
    capacity = cap
    tracks = num_tracks

    for l in loads :
        if capacity >= l: 
            capacity -= l
            num += 1
        else:
            if tracks > 1:
                tracks -= 1
                capacity = cap

                if capacity >= l:
                    capacity -= l
                    num += 1
                else:
                    break
            else:
                break
    return num

def Main():
    N, K = map(int, input().split())
    loads = list()

    for i in range(N):
        l = int(input())
        loads.append(l)

    pl = 0
    pr = sum(loads)

    pm = int( (pl + pr)/2.0 ) + 1
    pm_ = 0

    while pl < pr :
        pm = math.ceil( (pl + pr)/2.0 )

        nl = search( pl, loads, K)
        nm = search( pm, loads, K)
        nr = search( pr, loads, K)

        if pm_ == pm:
            print(pm)
            break

        if nm == nr :
            pl = pl
            pr = pm
            pm_ = pm
        else :
            pl = pm
            pr = pr
            pm_ = pm

Main()
