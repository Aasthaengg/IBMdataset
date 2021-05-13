N=int(input())
pre=0
ans=0
for i in range(N):
    a=int(input())
    if i==0 and a!=0:
        print(-1)
        exit()
    if i>0:
        if pre+1<a:
            print(-1)
            exit()
        if a==pre+1:
            ans+=1
        elif pre>=a:
            ans+=a
    pre=a
print(ans)