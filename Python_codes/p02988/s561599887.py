n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    m=min(l[i],l[i-1],l[i+1])
    x=max(l[i],l[i-1],l[i+1])
    if(m!=l[i] and x!=l[i]):
        c+=1
print(c)
