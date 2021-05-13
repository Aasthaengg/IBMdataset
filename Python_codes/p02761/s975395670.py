n,m=map(int,input().split())
SC=[list(map(int,input().split())) for _ in range(m)]
ans=-1
if n==1:
    r=range(10)
elif n==2:
    r=range(10,100)
else:
    r=range(100,1000)
for i in r :
    i=str(i)
    for j ,k in SC:
        if i[j-1]!=str(k):
            break
    else:
        print(i)
        exit()
print(-1)