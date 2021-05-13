n=int(input())

from collections import deque

option=deque()
option.append("a")
ans=[]

while option:
    s=option.pop()
    if len(s)==n:
        ans.append(s)
        continue
    maxi=0
    for i in s:
        maxi=max(maxi,ord(i))
        
    for i in range(97,maxi+2):
        new_s=s+chr(i)
        if new_s not in option and len(new_s)<=n:
            option.append(new_s)

ans=sorted(ans)
for i in ans:
    print(i)