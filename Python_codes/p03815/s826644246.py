x=int(input())

a=x%11
if a==0:
    ans=x//11
    print(2*ans)
elif a>6:
    t=x//11
    ans=2*t+2
    print(ans)
else:
    t=x//11
    ans=2*t+1
    print(ans)