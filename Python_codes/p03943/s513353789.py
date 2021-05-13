A=list(map(int,input().split()))

max_des = max(A)

A.remove(max_des)

if sum(A)==max_des:
    print('Yes')
else:
    print('No')	