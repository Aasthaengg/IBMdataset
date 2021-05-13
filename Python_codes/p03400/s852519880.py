n=int(input())
d,x=map(int,input().split())
A=[ (int(input())) for i in range(n)]

for i in range(n):
    x+=1
    for j in range(1,d+1):
        if 1+j*A[i] <= d:
            x+=1
print(x)