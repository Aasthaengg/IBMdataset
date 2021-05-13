N=int(input())
A=list(map(int,input().split()))

F=0
K=1
b=A[0]

for a in A:
    if F==0:
        if b<a:
            F=1
            b=a
        elif b>a:
            F=-1
            b=a
    elif F==1 and b>a:
        K+=1
        F=0
    elif F==-1 and b<a:
        K+=1
        F=0
    b=a
print(K)
