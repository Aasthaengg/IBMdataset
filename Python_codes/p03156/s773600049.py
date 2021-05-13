# 2019/12/7

n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))

f,s,t=0,0,0
for e in p:
    if e<=a:f+=1
    elif b+1<=e:t+=1
    else:s+=1
print(min(f,s,t))