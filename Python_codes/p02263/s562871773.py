
A=input().split()
i=0
for j in range(len(A)):
    if A[i]=="+":
        r=int(A[i-2])+int(A[i-1])
        A[i]=r
        del(A[i-2])
        del(A[i-2])
        i-=2
    if A[i]=="-":
        r=int(A[i-2])-int(A[i-1])
        A[i]=r
        del(A[i-2])
        del(A[i-2])
        i-=2
    if A[i]=="*":
        r=int(A[i-2])*int(A[i-1])
        A[i]=r
        del(A[i-2])
        del(A[i-2])
        i-=2
    i+=1

print(r)

