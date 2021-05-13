n,k = map(int,input().split())
s= input()
if n==1:
    print(1)
    exit()

ls = []
cnt=[0,0]
prev=int(s[0])
if prev==0:
    ls.append(0)
cnt[prev]+=1
for i in range(1,n):
    now= int(s[i])
    cnt[now] +=1
    if now!=prev:
        ls.append(cnt[prev])
        cnt[prev]=0
    prev = now
if cnt[now]!=0:
    ls.append(cnt[now])
if s[-1] =="0":
    ls.append((0))

##ls --> 1010..101の順

l=len(ls)//2+1
p = 0
idx = 0
ans =ls[0]
temp=ls[0]
for i in range(1,l):
    temp+= ls[2*i]+ls[2*i-1]
    ans = max(temp,ans)
    p+=1
    if p>=k:
        temp -= (ls[2*idx]+ls[2*idx+1])
        idx+=1
print(ans)
