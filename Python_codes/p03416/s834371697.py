a,b=map(int,input().split())
ans=0
while a!=b+1:
    str1=str(a)
    if str1[0]==str1[4] and str1[1]==str1[3]:
        ans+=1
    a+=1
print(ans)
