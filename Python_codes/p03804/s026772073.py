n,m=map(int,input().split())
A=[input() for _ in range(n)]
B=[input() for _ in range(m)]
#print(B)
for i in range(n-m+1):
    for j in range(n-m+1):
        tmp=["" for i in range(m)]
        for k in range(m):
            for r in range(m):
                tmp[k]+=A[i+k][j+r]
        #print(tmp)
        if tmp == B:
            print("Yes")
            exit()
print("No")