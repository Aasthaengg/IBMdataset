n=int(input())
A=list(map(int,input().split()))
D=[abs(A[0])]
for i in range(n-1):
    D.append(abs(A[i+1]-A[i]))
D.append(abs(A[-1]))
s=sum(D)
for i in range(n):
    c=s
    c-=D[i]+D[i+1]
    if i==0:
        c+=abs(A[1])
    elif i==n-1:
        c+=abs(A[-2])
    else:
        c+=abs(A[i+1]-A[i-1])
    print(c)