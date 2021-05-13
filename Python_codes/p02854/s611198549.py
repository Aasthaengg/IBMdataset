N=int(input())
A=list(map(int,input().split()))
x=sum(A)
y=10**19
a=0
for i in range(N):
    a+=A[i]
    if y>abs(x-2*a):#2区間の差
        y=abs(x-2*a)
        
    else:
        break

print(y)