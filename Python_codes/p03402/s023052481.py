A,B=map(int,input().split())
C=[[0 for i in range(100)] for i in range(100)]
for i in range(50,100):
    for j in range(100):
        C[i][j]=1
k=0
for i in range(50):
    for j in range(100):
        if (i*j)%2 ==1:
            if k<A-1:
                C[i][j]=1
                k+=1
            else:
                break
k=0
for i in range(50,100):
    for j in range(100):
        if (i*j)%2 ==1:
            if k<B-1:
                C[i][j]=0
                k+=1
            else:
                break
print(100,100)
for i in range(100):
    st=""
    for j in range(100):
        if C[i][j]==0:
            st+="#"
        else:
            st+="."
    print(st)
