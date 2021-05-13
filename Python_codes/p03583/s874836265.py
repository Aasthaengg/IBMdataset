N=int(input())

def isOK(n,w):
    if 4*n*w-N*w-N*n==0:
        return False
    if N*n*w%(4*n*w-N*w-N*n)==0:
        h=N*n*w//(4*n*w-N*w-N*n)
        if 0<h:
            return h
    return False

for i in range(1,3501):
    for j in range(1,3501):
        if isOK(i,j):
            print(i,j,isOK(i,j))
            exit()
