H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))
table=[[0 for _ in range(W)] for _ in range(H)]
changeflag=0
#print(table)
i=0
back=0
zagflag=0
if H%2==0:
   j=0
   back=0
   zagflag=0
else:
    j=W-1
    back=1
    zagflag=1
allcnt=0
colorid=1
cnt=0
while (j!=0)or(i!=H-1):
    #print(i,j,back)
    if cnt==a[colorid-1]:
        colorid=colorid+1
        cnt=0
    table[i][j]=colorid
    cnt=cnt+1
    allcnt=allcnt+1
    if (((zagflag%2==1)and(j==0))or((zagflag%2==0)and(j==W-1)))and(allcnt!=0):
        i=i+1
        back=(back+1)%2
        zagflag=zagflag+1
    else:
        if back==0:
            j=j+1
        else:
            j=j-1
    #print(table,colorid,cnt)
    #input()
table[H-1][0]=N
for i in range(H):
    print(*table[i],sep=" ")

