N, A, B, C = map(int, input().split())
L = [0]*N
for i in range(N):
  L[i] = int(input())

import itertools
bambuu = [[0,0,0] for _ in range(4**N)]
for i,pro in enumerate(itertools.product(['A','B',"C",'D'], repeat=N)):
    lisA = [L[j] for j in range(N) if pro[j]=='A']
    lisB = [L[j] for j in range(N) if pro[j]=='B']
    lisC = [L[j] for j in range(N) if pro[j]=='C']
    sumA = [sum(lisA),(len(lisA)-1)*10]
    sumB = [sum(lisB),(len(lisB)-1)*10]
    sumC = [sum(lisC),(len(lisC)-1)*10]
    bambuu[i-1] = [sumA,sumB,sumC]

ans = 10000
for sA,sB,sC in bambuu:
    if sA[0]>0 and sB[0]>0 and sC[0]>0:
        mp_total = abs(A-sA[0])+abs(B-sB[0])+abs(C-sC[0])+sA[1]+sB[1]+sC[1]
        if mp_total < ans:
            #record = [sA,sB,sC]
            ans = mp_total
#print(record)
print(ans)
#print(*ans, sep='\n')