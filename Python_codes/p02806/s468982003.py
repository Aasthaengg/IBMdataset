n=int(input())
play=[]
for i in range(n):
    s,t=map(str,input().split())
    play.append([s,t])
x=input()
ans=0
flag=False
tmp=0
for i in range(n):
    if play[i][0]==x:
        flag=True
        tmp=int(play[i][1])
    if flag:
        ans+=int(play[i][1])

print(ans-tmp)