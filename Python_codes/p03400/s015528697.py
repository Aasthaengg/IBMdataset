n=int(input())
d,x=map(int,input().split())
A=[]
for i in range(n):
    a=int(input())
    A.append(a)
q=x
for i in range(n):
    q+=1
    for j in range(1,d+1):
        if 1+j*A[i] <= d:
            q+=1
print(q)