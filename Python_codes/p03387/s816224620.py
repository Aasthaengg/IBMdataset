l=list(map(int,input().split()))
l.sort()
cnt=0
cnt+=l[2]-l[1]
l[0]+=l[2]-l[1]
l[1]=l[2]
if (l[1]-l[0])%2!=0:
    l[1]+=1
    l[2]+=1
    cnt+=1
cnt+=(l[1]-l[0])//2
print(cnt)