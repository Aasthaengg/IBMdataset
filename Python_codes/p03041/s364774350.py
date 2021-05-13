a,b=map(int,input().split())
s=list(input())
wd=''
cnt=1
for i in s:
    if cnt==b:
        cnt+=1
        wd+=(i.lower())
    else:
        cnt+=1
        wd+=(i)
print(wd)