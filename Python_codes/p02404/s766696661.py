while True:
    a = input()
    b = a.split(' ')
    H = int(b[0])
    W = int(b[1])
    if H == 0 and W == 0:
        break
    print('#'*W)
    for i in range(H-2):
        print('#'+'.'*(W-2)+'#')
    print('#'*W)
    print()