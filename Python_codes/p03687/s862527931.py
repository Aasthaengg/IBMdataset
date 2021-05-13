from math import ceil

s=input()
x='abcdefghijklmnopqrstuvwxyz'
ans=1000


def greedy(i,s,cnt):
    if s.count(s[0])==len(s):
        return cnt
    t=''
    for j in range(len(s)-1):
        if s[j]==i or s[j+1]==i:
            t+=i
        
        else:
            t+=s[j]
    
    return greedy(i,t,cnt+1)


for i in x:
    ans=min(ans,greedy(i,s,0))


print(ans)
