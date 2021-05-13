N=int(input())
*A,=map(int,input().split())
A=A[::-1]
B=[0]*N

i=1
count=0
while count<N:
    if count%2==0:
        B[i-1]=A[count]
    else:
        B[-i]=A[count]
        i+=1
    count+=1

print(*B)