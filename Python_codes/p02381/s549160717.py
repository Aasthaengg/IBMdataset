while True:
    try:
        n = int(input())
        if n==0:
            break
        S = list(map(int,input().split()))
    except:
        break
    mean = sum(S)/len(S)
    tmp = 0
    for s in S:
        tmp += ((s-mean)**2)/n
    print(tmp**0.5)
