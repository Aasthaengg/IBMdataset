import sys
a=list(map(int,input().split()))
a.sort()
ans=0
while True:
    if a[0]==a[1]==a[2]:
        print(ans)
        sys.exit()
    if a[0]<a[1]:
        a[0]+=2
        ans+=1
        a.sort()
        if a[0]==a[1]==a[2]:
            print(ans)
            sys.exit()
    if a[0]==a[1]:
        a[0]+=1
        a[1]+=1
        ans+=1
        a.sort()
        if a[0]==a[1]==a[2]:
            print(ans)
            sys.exit()