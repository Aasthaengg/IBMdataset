#入力
N,T=[int(x) for x in input().split()]
A=[int(x) for x in input().split()]

max=N-1
low=0
maxnum=0
dif = -1

for i in range(1,len(A)):
    if(A[low]>A[i]):
        low=i
    else:
        if(A[i] - A[low] > dif):
            dif=A[i] - A[low]
            maxnum=1
        elif(dif==A[i] - A[low]):
            maxnum+=1

print(maxnum)