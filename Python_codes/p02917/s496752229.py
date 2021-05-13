N=int(input())
*B,=map(int,input().split())


x=[0]*N
x[0]=B[0]
x[-1]=B[-1]
for i in range(1,N-1):
    x[i]=min(B[i-1],B[i])
print(sum(x))