t1,t2=map(int,input().split())

a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

a=a1-b1
b=a2-b2
#print(a,b)

ans=0

if(a*b>0):
    ans=-1
else:
    go=a*t1+b*t2
    if(go*a>0):
        ans=0
    elif(go==0):
        ans=-10
    else:
        kai=a*t1
        if(go<0):
            go*=-1
        if(kai<0):
            kai*=-1
        #print(kai//go)
        if(kai%go==0):
            ans=(kai//go)*2
        else:
            ans=(kai//go)*2+1

if(ans==-1):
    print(0)
elif(ans==-10):
    print("infinity")
else:
    print(ans)