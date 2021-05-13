N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))

D.sort()
T.sort()
if N<M:
    print("NO")
    exit()

flag=True
cnt=0
count=0
for i in range(M):
    if cnt>=N:
        flag=False
        break
    chk=0
    while(D[cnt]!=T[i]):
        cnt+=1
        chk=1
        if cnt==N:
            flag=False
            break
    if cnt>=N:
        break
    if D[cnt]==T[i]:
        count+=1
    cnt+=1

if count==M:
    pass
else:
    flag=False

if flag:
    print("YES")
else:
    print("NO")