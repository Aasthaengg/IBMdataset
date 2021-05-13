n=int(input())
a=list(map(int,input().split()))

breaking=0
cnt=1
for i in a:
    if i==cnt:
        cnt+=1
    else:
        breaking+=1
        
if breaking==len(a):
    print(-1)
else:
    print(breaking)