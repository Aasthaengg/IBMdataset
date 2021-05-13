A=list(input())
for i in range(4):
    A[i]=int(A[i])
for i in range(8):
    x=A[0]
    for j in range(3):
        if (i//(2**j))%2==1:
            x+=A[j+1]
        else:
            x-=A[j+1]
    if x==7:
        print(A[0],end='')
        for j in range(3):
            if (i//(2**j))%2==1:
                print('+',end='')
            else:
                print('-',end='')
            print(A[j+1],end='')
        print('=7')
        break
