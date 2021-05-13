def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
    
n=I()
a=LI()
ans=0
pre=None
for i in a:
    if pre==None:
        pre=i
        c=1
        continue
    if i==pre:
        c+=1
    else:
        ans+=c//2
        c=1
    pre=i
ans+=c//2
print(ans)