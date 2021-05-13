n=int(input())
a=list(map(int,input().split()))
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
cnt,sur=0,0
for i in dic.values():
    if i%2==0:
        cnt+=(i-1)//2
        sur+=1
    else:
        cnt+=i//2
print(n-cnt*2-(sur+1)//2*2)