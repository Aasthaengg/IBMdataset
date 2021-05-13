i = list(map(int, input().split()))

H = i[0]
W = i[1]

while H != 0 or W != 0 :
    for i in range(H) :
        for j in range(W) :
            print('#', end='')
        if W != 0 :
            print()
    print()
    i = list(map(int, input().split()))

    H = i[0]
    W = i[1]