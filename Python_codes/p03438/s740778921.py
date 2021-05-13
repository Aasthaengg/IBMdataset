import sys
readline = sys.stdin.buffer.readline
n = int(readline())
ab = [[0,0] for i in range(n)]
lsta = list(map(int,input().split()))
lstb = list(map(int,input().split()))
for i in range(n):
    ab[i][0] = lsta[i]
    ab[i][1] = lstb[i]

bstock = 0

move = sum(lstb) - sum(lsta)

if move == 0:
    if lsta == lstb:
        print("Yes")
    else:
        print("No")
    exit()

ab.sort()
i = 0
while i < n-1:
    if ab[i][0] > ab[i][1]: #bstockを使う
        if ab[i][0] > ab[i][1]+bstock:
            print("No")
            exit()
        else:
            bstock -= ab[i][0]-ab[i][1]
    elif ab[i][0]%2 == ab[i][1]%2:
        bstock += (ab[i][1]-ab[i][0])//2
        move -= (ab[i][1]-ab[i][0])//2
    else:
        move -= (ab[i][1]-ab[i][0])//2 + 1
        bstock += (ab[i][1]-ab[i][0])//2
    if move < 0 or bstock < 0:
        print("No")
        exit()    
    i+= 1

if ab[-1][0]+(move*2)==ab[-1][1]+move+bstock:
    print("Yes")
else:
    print("No")
