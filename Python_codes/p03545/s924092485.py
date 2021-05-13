import itertools as itr

A=list(map(int,input()))
b=list(itr.product(range(2),repeat=3))

for i in b:
    i=['+' if j==1 else '-' for j in i]
    ans=A[0]

    for j in range(3):
        if i[j]=='+':
            ans+=A[j+1]
        else:
            ans-=A[j+1]

    if ans==7:
        C=[]
        for j in range(3):
            C.append(A[j])
            C.append(i[j])
        C.append(A[3])
        C.append('=7')
        print(''.join(map(str,C)))
        exit(0)   

print(-1)