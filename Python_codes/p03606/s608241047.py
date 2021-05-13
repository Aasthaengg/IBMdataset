N=int(input())
lr=[]
A=[]
for i in range(N):
    lr.append(list(map(int,input().split())))
for i in range(N):
    A.append(lr[i][1]-lr[i][0]+1)
print(sum(A))