import numpy as np

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

#def numsearch(list):
    #for i in list:
        #print(i)
        #if (i+1)/2 not in list:
            #list.remove(i)
    #return list

def main():
    Q = int(input())
    list = seachPrimeNum(100000)
    #フラグを立てるよ
    check = [0]*100001
    primeCheck = [0]*100001
    for i in list:
        primeCheck[i] = 1
    for i in list:
        if i == 2:
            continue
        tmp = int((i+1)/2)
        if primeCheck[tmp] == 1:
            check[i] = 1
    #答えを求めるための累積和
    c = [0]*100001
    c[0] = 0
    for i in range(1,100001,1):
        #print(i)
        if check[i] == 1:
            c[i] = c[i-1]+1
        else:
            c[i] = c[i-1]
    #print(c)
    for i in range(Q):
        l,r = map(int,input().split())
        print(c[r]-c[l-1])

main()
