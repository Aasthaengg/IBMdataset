#ABC084D
def main():
    import sys
    Q = int(sys.stdin.readline())
    LR = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]
    #print(LR)
    
    check = [1 for _ in range(10**5+1)]
    check[0], check[1] = 0, 0
    for i in range(2, 10**5+1):
        if check[i] ==0:
            continue
        elif check[i] ==1:
            for j in range(2*i, 10**5+1, i):
                check[j] =0
    check2 = check.copy()
    for i in range(2, 10**5+1):
        if check[i]==1:
            #print((i+1)/2, check[(i+1)//2])
            if (i+1)%2==0 and check[(i+1)//2] ==1:
                continue
            else:
                check2[i] = 0
    
    #累積和
    for i in range(1, 10**5+1):
        check2[i] = check2[i-1] + check2[i]
    #print(check2)
    for lr in LR:
        print(check2[lr[1]] - check2[lr[0]-1])
                


if __name__ =='__main__':
    main()