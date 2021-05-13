n,m = map(int,input().split())
c = [list(map(int,input().split())) for i in range(n)]
ca = sorted(c,key=lambda x:x[0])

import sys
if n ==1:
    print(ca[0][0]*ca[0][1])
    sys.exit()
money = 0
i = 0
num = 0
while True:
    #print(str(i)+"だよ")
    if num + ca[i][1] < m:
        num += ca[i][1]
        money += ca[i][0] * ca[i][1]
        i += 1
        #print(num,money)
    else:
        money += ca[i][0]*(m-num)
        break    
print(money)