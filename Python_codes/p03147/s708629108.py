import math
N = int(input())
hs = list(map(int,input().split()))
c = 0
while True:
    pmi = 101
    start = 0
    flag = True
    for i in range(N):
        if hs[i] == 0:
            if pmi == 101:
                start += 1
                continue
            for j in range(start,i):
                hs[j] -= pmi
            #print(hs)
            c += pmi
            start = i+1
            pmi = 101
        else:
            flag = False
            pmi = min(pmi, hs[i])
    if flag:
        break
    else:
        if pmi != 101:
            for i in range(start,N):
                hs[i] -= pmi
            c += pmi
print(c)