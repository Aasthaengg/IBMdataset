import sys
input=sys.stdin.readline
n=int(input())
l=[int(input()) for i in range(n)]
if l[0]!=0:
    print(-1)
    quit()
l.reverse()
l+=[0]
ans=0
i=0
while i<n-1:
    if l[i]>n-i-1:
        print(-1)
        quit()
    if l[i+1]+1==l[i]:
        ans+=l[i]
        while l[i+1]+1==l[i]:
            i+=1
        i+=1
    elif l[i+1]+1<l[i]:
        print(-1)
        quit()
    else:
        ans+=l[i]
        i+=1
print(ans)