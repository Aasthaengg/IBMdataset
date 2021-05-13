n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(b)>sum(a):
    print(-1)
    exit()
p=[]
m=[]
sub=[]
for i in range(n):
    s=a[i]-b[i]
    if s>0:
        p.append(s)
    elif s<0:
        m.append(s)
p.sort(reverse=True)
ans=len(m)+min(len(m),1)
cnt=sum(m)
j=0
while cnt<0:
    if cnt+p[j]>=0:
        cnt+=p[j]
    else:
        cnt+=p[j]
        j+=1
        ans+=1
print(ans)
