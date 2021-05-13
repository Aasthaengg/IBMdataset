h, w = list(map(int, input().split()))

while h != 0 or w != 0 :

    judgeChange = 0

    for i in range(h) :
        for j in range(w) :
            if j % 2 == judgeChange:
                print('#', end = '')
            else :
                print('.', end = '')
        print()
        
        if judgeChange == 1 :
            judgeChange = 0
        else :
            judgeChange = 1
    print()
    h, w = list(map(int, input().split()))