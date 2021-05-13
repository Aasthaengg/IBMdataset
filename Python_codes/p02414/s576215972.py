n, m, l = map(int,input().split())
A=[]
B=[]
ans=[[] for i in range(n)]
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(m):
    B.append(list(map(int, input().split())))
for i in range(n):
    for k in range(l):
        temp=0
        for j in range(m):
            temp+=A[i][j]*B[j][k]
        ans[i].append(temp)
[print(" ".join(map(str, x))) for x in ans]