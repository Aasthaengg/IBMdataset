def main():
    n = int(input())
    Mtx = list(map(int, input().split()))
    
    showMtx(Mtx)
    for i in range(1,n):
        for j in range(i,0,-1):
            if Mtx[j] < Mtx[j-1]:
                Mtx[j-1], Mtx[j] = Mtx[j], Mtx[j-1]
            # print(i, j, sep=', ')
        showMtx(Mtx)
                

def showMtx(Mtx):    
    q = len(Mtx)
    for i in range(q):
        if i != q - 1:
            print(Mtx[i], sep=' ', end=' ')
        else:
            print(Mtx[i])



if __name__ == '__main__':
    main()

