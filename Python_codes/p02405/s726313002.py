while True:
    H, W = [int(i) for i in input().split()]
    if H ==0 and W ==0:
        break
    for i in range(2, H+2):
        if i%2 ==0:
            for k in range(1,W+1):
                if k%2 ==0:
                    print('.',end='')
                else:
                    print('#',end='')
            print()
        else:
            for h in range(1,W+1):
                if h%2 ==0:
                    print('#',end='')
                else:
                    print('.',end='')
            print()
    print()