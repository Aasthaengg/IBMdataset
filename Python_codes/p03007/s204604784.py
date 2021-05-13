
from collections import deque
N=int(input())
A=list(map(int, input().split()))

# プラス　マイナス引いていく
plus=[]
minus=[]
zeros=[]
for a in A:
    if a==0:
        zeros.append(a)
    elif a>=1:
        plus.append(a)
    else:
        minus.append(a)
plus=sorted(plus)
minus=sorted(minus)
zeros=sorted(zeros)
ans=[]
if plus and minus:
    while len(plus)>1:
        now=plus.pop()
        ans.append((minus[0],now))
        minus[0]-=now
    while len(zeros)>0:
        now=zeros.pop()
        ans.append((plus[0],now))
    while len(minus)>1:
        now=minus.pop()
        ans.append((plus[0],now))
        plus[0]-=now
    ans.append((plus[0],minus[0]))
    ansnum=plus[0]-minus[0]
else:
    ansnum=0
    if len(plus)==0:
        if zeros:
            core=zeros.pop()
        else:
            core=minus.pop()
        while len(minus)>0:
            now=minus.pop()
            ans.append((core,now))
            core-=now
        ansnum=core
    else:
        if zeros:
            core=zeros.pop()
        else:
            plus=deque(plus)
            core=plus.popleft()
        while len(plus)>1:
            now=plus.pop()
            ans.append((core,now))
            core-=now
        ans.append((plus[0],core))
        ansnum=plus[0]-core
        core=ansnum
    while len(zeros)>0:
        now=zeros.pop()
        ans.append((core,now))
    
    

print(ansnum)
for t in ans:
    x,y=t
    print(x,y)