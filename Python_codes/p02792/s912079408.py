n=int(input())

def pair(x):
    a=x%10
    b=int(str(x)[0])
    return (a,b)
dic={}
for i in range(1,n+1):
    p=pair(i)
    if(dic.get(p)==None):dic[p]=1
    else:dic[p]+=1
ans=0
for i in range(1,n+1):
    a,b=pair(i)
    p=(b,a)
    if(not dic.get(p)==None):ans+=dic[p]
print(ans)