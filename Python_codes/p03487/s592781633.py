n=int(input())
a=list(map(int,input().split()))

dic={}
for i in range(n):
    if dic.get(a[i])==None:
        dic[a[i]]=1
    else:
        dic[a[i]]+=1

ans=0
for key,number in dic.items():
    if number<key:
        ans+=number
    else:
        ans+=number-key
print(ans)
