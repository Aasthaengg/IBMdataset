n=input()
a = list(map(int,input().split()))

def chk(a,t):
    ans=0
    x=0
    for i in a:
        x+=i
        if t and x<1:
            ans+=1-x
            x=1
        elif not t and x>-1:
            ans+=x+1
            x=-1
        t= not t
    return ans

print(min(chk(a,True),chk(a,False)))
