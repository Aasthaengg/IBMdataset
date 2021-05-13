import sys
input=sys.stdin.readline

n,m,q=map(int,input().split())
T=[]
for i in range(m):
    l,r=map(int,input().split())
    T.append([l-1,r-1])

C=[[0]*n for i in range(n)] #C[始点][終点]=個数
for t in T:
    C[t[0]][t[1]]+=1

A=[[0]*n for i in range(n)] #A[始点][終点]=区間内の合計
for i in range(1,n+1): #iは区間の長さ
    for j in range(n-i+1): #jからj+i-1まで
        if i==1:
            A[j][j]=C[j][j]
        elif i==2:
            A[j][j+1]=A[j][j]+A[j+1][j+1]+C[j][j+1]
        else:
            A[j][j+i-1]=A[j][j+i-2]+A[j+1][j+i-1]-A[j+1][j+i-2]+C[j][j+i-1]

for i in range(q):
    a,b=map(int,input().split())
    print(A[a-1][b-1])
