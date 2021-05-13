A = list(input())
sign = ['+','-']
for i in range(2):
    for j in range(2):
        for k in range(2):
            if eval(A[0]+sign[i]+A[1]+sign[j]+A[2]+sign[k]+A[3]) == 7:
                print('{}{}{}{}{}{}{}=7'.format(A[0],sign[i],A[1],sign[j],A[2],sign[k],A[3]))
                exit()