N=int(input())
D,X=map(int,input().split())
A=list()
chocolate=0
for i in range(N):
    A.append(int(input()))
for i in range(D):
    for j in A:
        if ((i+1)%j==1)|(j==1):
            chocolate+=1
print(chocolate+X)