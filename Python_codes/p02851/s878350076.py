n,k=map(int,input().split())
a=list(map(lambda x:(int(x)-1)%k,input().split()))
s=[0]
#print(a)
for i in a:
    s.append((s[-1]+i)%k)
#print(s)
mp={}
ans=0
for i in range(len(s)):
    if i-k>=0:
        mp[s[i-k]]-=1
    if s[i] in mp:
        ans+=mp[s[i]]
    if s[i] in mp:
        mp[s[i]]+=1
    else:
        mp[s[i]]=1
    #print(i,ans)
print(ans)
#ans+=sum(list(map(lambda x: x==0,s)))
#print(ans)
