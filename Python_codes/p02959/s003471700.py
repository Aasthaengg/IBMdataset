N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

count=0

D=[A[0]]

for i in range(N):
    s=B[i]-D[i]
    if s>0:
        d=A[i+1]-s
        if d>0:
            d=d
            count+=B[i]
        else :
            d=0
            count+=D[i]+A[i+1]
    else:
        d=A[i+1]
        count+=B[i]
    D.append(d)

print(count)