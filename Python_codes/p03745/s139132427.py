def nyu():
    N = int(input())
    A = list(map(int,input().split()))

    return N,A

def kansu(LN,LA):
    highflg = False
    lowflg = False
    count = 1

    for n in range(LN-1):
        if LA[n] == LA[n+1]:
            continue
        elif LA[n] < LA[n+1]:
            highflg = True
            if lowflg == True:
                count += 1
                lowflg = False
                highflg = False
        else:
            lowflg = True
            if highflg == True:
                count += 1
                lowflg = False
                highflg = False
    
    print(count)






N,A = nyu()
kansu(N,A)