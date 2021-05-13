Slist=input()
Slist=Slist.replace("><",">,<").split(",")
ans=0
for S in Slist:
    a=S.count("<")
    b=S.count(">")
    n=max(a,b)
    m=len(S)-n
    ans=ans+n*(n+1)//2+(m-1)*m//2
print(ans)