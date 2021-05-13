N=int(input())
b=list(map(int,input().split()))
ans=[]
turn=N
while(b):
    last=-1
    for i in range(len(b)):
        if i+1==b[i]:
            last=i
    if last==-1:
        print(-1)
        exit()
    ans.append(last+1)
    del b[last]
    
print(*ans[::-1],sep='\n')