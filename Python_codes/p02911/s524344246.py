N,K,Q = map(int,input().split())
lsN = [K-Q]*N
for i in range(Q) :
    p = int(input())
    lsN[p-1] = lsN[p-1]+1

for i in lsN:
    if i > 0:
        print('Yes')
    elif i <= 0:
        print('No')