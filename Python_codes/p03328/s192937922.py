a,b=map(int,input().split())
l=[0]*999
for i in range(1,1000):
    l[i-1]=(i*(i+1)//2)
#print(l)
for i in range(998):
    if (b-a)==l[i+1]-l[i]:
        ans=l[i]-a
print(ans)