N=int(input())
D,X=map(int,input().split())
A=[]
for i in range(N):
    A+=[int(input())]
eaten=0
for i in range(D):
    for j in range(N):
        if i%A[j]==0:
            eaten+=1
print(X+eaten)