H,W=map(int,input().split())
s=[]
count=[[10**9 for _ in range(W)] for i in range(H)]
for i in range(H):
    S=input()
    s.append(S)
if s[0][0]=="#":
    count[0][0]=1
else:
    count[0][0]=0
for i in range(H):
    for j in range(W):
        if i==0 and j==0:
            continue
        val1=10**9
        val2=10**9
        if i==0:
            pass
        else:
            val1=count[i-1][j]
            if s[i][j]=="#" and s[i-1][j]==".":
                val1+=1
        if j==0:
            pass
        else:
            val2=count[i][j-1]
            if s[i][j]=="#" and s[i][j-1]==".":
                val2+=1
        count[i][j]=min(val1,val2)
print(count[-1][-1])