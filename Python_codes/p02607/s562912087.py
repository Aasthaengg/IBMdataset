N=int(input())
A=list(map(int,input().split()))
b=0
for i in range(len(A)):
    if (i+1)%2==1 and A[i]%2==1:
        b+=1
print(b)