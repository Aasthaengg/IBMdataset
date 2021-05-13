while True:
    H,W=map(int,input().split())
    array='#.'
    if H == 0 and W == 0:
        break
    else:
        for i in range(H):
            print(array*(int(W/2)) + array[0]*(W%2))
            array=array[1]+array[0]
    print('') 