n=int(input())
a=list(map(int,input().split()))
l=[0]*n
for i in range(n):
    l[a[i]]+=1
#print(l)
if n%2==1:
    if l[0]!=1:
        print(0)
        exit()
ans=1
for i in range(n):
    if n%2==0:
        if i%2==0:
            if l[i]!=0:
                print(0)
                exit()
    else:
        if i%2==1:
            if l[i]!=0:
                print(0)
                exit()
    
    if l[i]==2:
        ans*=2
    elif l[i]>2:
        print(0)
        exit()
    ans%=(10**9 +7)
print(ans)