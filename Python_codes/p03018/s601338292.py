from collections import deque
s=list(input())
d=deque()
n=len(s)
acount=0
cnt=0
for i in range(n):
    d.append(s[i])
i=0
while i<n:
    if s[i]=="A":
        acount=acount+1
    elif (i<n-1)and(acount>0)and(s[i]=="B")and(s[i+1]=="C"):
        cnt=cnt+acount
        i=i+1
    else:
        acount=0
    i=i+1
    #print(acount,cnt)
    #input()
print(cnt)