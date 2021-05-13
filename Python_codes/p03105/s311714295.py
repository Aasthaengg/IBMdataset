A,B,C = map(int,input().split())

nec = A*C
if(B>=nec):
    print(C)
else:
    i = C
    while all:
        if(A*i <= B):
            break
        else:
           i -= 1

    print(i)
