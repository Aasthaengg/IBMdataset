def resolve():
    N = int(input())
    H = list(map(int, input().split()))
    lower = True
    for i in range(N-1):
        if H[i] > H[i+1]:
            if H[i] - H[i+1] == 1 and lower is True:
                lower = False
            else:
                print("No")
                return
        elif H[i] == H[i+1]:
            pass
        else:
            lower = True

    print("Yes")


    
if '__main__' == __name__:
    resolve()