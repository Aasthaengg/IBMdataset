while True:
    x = input().split()
    x_int = [int(i) for i in x]

    if x_int[0] == 0 and x_int[1] == 0:
        break
    for i in range(x_int[0]):
        for j in range(x_int[1]):
            if i % 2 == 0 :
                if j % 2 == 0:
                    print('#',end='')
                else:
                    print('.',end='')
            else:
                if j % 2 == 0:
                    print('.',end='')
                else:
                    print('#',end='')
        print()
    print()