n=int(input())
dic={}
cnt=1
s=[input() for i in range(n)]
for i in s:
    if i in dic:
        dic[i]+=1
        cnt=max(cnt,dic[i])
    else:
        dic[i]=1
ans=[]
for i in s:
    if dic[i]==cnt:
        ans.append(i)
ans=list(set(ans))
ans.sort()
for i in ans:
    print(i)
