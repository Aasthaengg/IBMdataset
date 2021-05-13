n,x,y = map(int, input().split())

kyori=[0]*10**7

import itertools
for seq in itertools.combinations(range(1,n+1),2):
    kyori_niten=seq[1]-seq[0]
    kyori_niten=min(kyori_niten,abs(x-seq[0])+abs(y-seq[1])+1)

    kyori[kyori_niten]+=1

for i in range(1,n):
    print(kyori[i])