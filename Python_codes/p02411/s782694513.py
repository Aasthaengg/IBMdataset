while True:
    m, f, r = map(int, input().split())

    if(m == -1 and f == -1 and r == -1):
        break

    total = m + f
    if(m == -1 or f == -1):
        print('F')
    elif(total >= 80):
        print('A')
    elif(65 <= total and total < 80):
        print('B')
    elif(50 <= total and total < 65):
        print('C')
    elif(30 <= total and total < 50):
        if(50 <= r):
            print('C')
        else:
            print('D')
    else:
        print('F')

