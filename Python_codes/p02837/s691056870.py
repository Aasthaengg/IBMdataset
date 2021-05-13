n=int(input())
state=[[] for _ in range(n)]
for _ in range(n):
    a=int(input())
    for i in range(a):
        x,y=map(int,input().split())
        state[_].append([x,y])
ans=0
for i in range(2**n):
    temp=[0]*n
    for j in range(n):
        if i&1: temp[j]=1
        i>>=1
    flag=1
    for k,s in enumerate(temp):
        if s==0: continue
        for st in state[k]:
            if temp[st[0]-1]!=st[1]:
                flag=0
                break
            if not flag: break
    if flag:
        cnt=temp.count(1)
        if cnt>ans: ans=cnt
print(ans)