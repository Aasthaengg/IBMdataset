n,m=map(int,input().split())
s=["0"]*n
for i in range(m):
    a,b=map(int,input().split())
    if s[a-1]=="0":
        s[a-1]=b
    elif s[a-1]!=b:
        print(-1)
        exit()
if n>1 and s[0]=="0":
    s[0]="1"
if n>1 and s[0]==0:
    print(-1)
    exit()
print(*s, sep="")