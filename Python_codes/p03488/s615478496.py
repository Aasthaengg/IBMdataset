now=0
idx=-1
data=[[],[]]
cnt=0
for s in input():
    if s=='F':
        cnt+=1
    elif s=='T':
        if idx==-1:
            now+=cnt
            cnt=0
            idx=1
        elif idx==0:
            data[0].append(cnt)
            cnt=0
            idx=1
        elif idx==1:
            data[1].append(cnt)
            cnt=0
            idx=0
if idx==-1:
    now+=cnt
else:
    data[idx].append(cnt)
def solve(target,move):
    dp={0,}
    for m in move:
        dpc=dp.copy()
        dp=set()
        for k in dpc:
            dp|={k-m,k+m}
    if target in dp:
        return True
    return False
x,y=map(int,input().split())
x-=now
if solve(x,data[0]) and solve(y,data[1]):
    print('Yes')
else:
    print('No')
