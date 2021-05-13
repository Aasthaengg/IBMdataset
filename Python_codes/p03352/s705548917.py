import math

X = int(input())
ans = 1
flg = False
for i in range(X, 0, -1):
    if flg:
        break
    for j in range(2, int(math.sqrt(i)) + 1):
        temp = i
        while True:
            if temp % j != 0:
                break
            elif temp / j == 1:
                print(i)
                flg = True
            temp = temp // j
        if flg:
            break
if not flg:
    print(1)
