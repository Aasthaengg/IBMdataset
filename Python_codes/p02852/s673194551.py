n,m = map(int, input().split())
s = input()

cnt=0
for i in range(len(s)):
    if s[i]=="1":
        cnt+=1
        if cnt>=m:
            print(-1)
            exit()
    else:
        cnt=0

cnt=0
from collections import defaultdict
d = defaultdict(int)
d[cnt]=n
for i in reversed(range(len(s))):
    if d[cnt] - i > m:
        cnt+=1
    if s[i]=="0":
        d[cnt+1]=i
d[cnt+1]=0

ans=[]
for i in reversed(range(len(d)-1)):
    ans.append(d[i] - d[i+1])
print(*ans,sep=" ")