K=int(input())
A=list(map(int,input().split()))
MAX=2
MIN=2
A=A[::-1]
ans=0
for a in A:
    MIN=(MIN-1)//a*a+a
    if MIN>MAX:
        ans=-1
        break
    MAX=MAX//a*a+a-1
if ans==-1:
    print(-1)
else:
    print(str(MIN)+" "+str(MAX))