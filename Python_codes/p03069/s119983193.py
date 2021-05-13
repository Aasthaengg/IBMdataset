N=int(input())
S=input()
leftid=-1
rightid=-1
blcnt=0
whcnt=0
cnt=0
ans=float("inf")
#.*#*になれば良い
#左と右から黒石・白石の数を数えていき、
#"a1,a2,a3,...,aN"列から構成しうるN+1この".#"境界
#について境界右で白い部分と左で黒い部分を変更する必要があるため、その和の最小が答え
leftblack=[0]*N
rightwhite=[0]*N
if S[0]=="#":
    leftblack[0]=1
if S[N-1]==".":
    rightwhite[N-1]=1
for i in range(1,N):
    if S[i]=="#":
        leftblack[i]=leftblack[i-1]+1
    else:
        leftblack[i] =leftblack[i - 1]
#print(leftblack)
for i in range(N-1,0,-1):
    if S[i-1]==".":
        rightwhite[i-1]=rightwhite[i]+1
    else:
        rightwhite[i-1] = rightwhite[i]
#print(rightwhite)
leftblack.insert(0,0)
rightwhite.insert(N,0)
#print(leftblack)
#print(rightwhite)
for i in range(N+1):# ####→.###→→....を考える
    ans=min(ans,leftblack[i]+rightwhite[i])
print(ans)