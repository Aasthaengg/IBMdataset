if __name__ == '__main__':

    n = int(input())
    
    flg = False

    for i in range(0,101,4):
        for j in range(0,101,7):
            if i + j > 100:
                break
            if n - (i+j) == 0:
                flg = True
                break
        if flg:
            break

    if flg:
        print("Yes")
    else:
        print("No")
