A,B=map(int,input().split())
G=[[0]*100 for i in range(100)]
for i in range(50,100):
    G[i]=[1]*100
A-=1
B-=1
i=0
j=0
while(B):
    G[i][j]=1
    B-=1
    if j==98:
        j=0
        i+=2
    else:
        j+=2
i=51
j=0
while(A):
    G[i][j]=0
    A-=1
    if j==98:
        j=0
        i+=2
    else:
        j+=2
S=[]
print(100,100)
for i in range(100):
    s=""
    for j in range(100):
        if G[i][j]==0:
            s+="."
        else:
            s+="#"
    print(s)
