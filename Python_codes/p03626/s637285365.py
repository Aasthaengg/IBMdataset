n=int(input())
s1=input()
s2=input()
l=[]
old="hoge"
for i in range(n):
    if s1[i]==s2[i]:
        l.append(0)
    elif s1[i]!=old:
        l.append(1)
    old=s1[i]
ans=1
flag=2
INF=10**9+7
for i in l:
    if flag==1:
        if i==1:ans=ans*3%INF
    elif flag==0:ans=ans*2%INF
    else:
        if i==0:ans*=3
        else:ans*=6
    flag=i
print(ans)