n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

if sum(a)<sum(b):
    print(-1)
    exit()

c=[]
ans=0
count=0
for i in range(n):
    c.append(a[i]-b[i])
    if c[i]<0:
        ans+=1
        count+=c[i]
#print(count)
c.sort(reverse=True)
#print(ans)
i=0
while count<0:
    count+=c[i]
    ans+=1
    i+=1
    #print("DFGH")

print(ans)