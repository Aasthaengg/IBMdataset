#21 Next Prime
X=int(input())
num=X 
for _ in range(1000000):
    flg = True
    # 2からnumまでの数でわりきれるかどうか（True：どの数字でも割り切れなかったので、素数。False:素数じゃない）
    for i in range(2,num):
        if num%i==0:
            flg = False
            break
    
    if flg:
        print(num)
        break
    else:
        num+=1
        pass