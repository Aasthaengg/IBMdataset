
def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    


    out = []
    def move(x1,y1,x2,y2):
        A[y1][x1] -= 1
        A[y2][x2] += 1
        out.append('{} {} {} {}'.format(y1+1,x1+1,y2+1,x2+1))
    for i in range(H):
        if i & 1:
            for j in range(W-1):
                if A[i][j] & 1:
                    move(j,i,j+1,i)
            if A[i][W-1] & 1 and i < H-1:
                move(W-1,i,W-1,i+1)
        else:
            for j in range(W-1,0,-1):
                if A[i][j] & 1:
                    move(j,i,j-1,i)
            if A[i][0] & 1 and i < H-1:
                move(0,i,0,i+1)
    print(len(out))
    print('\n'.join(out))








main()