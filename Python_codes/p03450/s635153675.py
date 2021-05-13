import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

n,m=map(int,input().split())

lrd=[[] for _ in range(n)]

for _ in range(m):
    l,r,d=map(int,input().split())
    lrd[l-1].append((r-1,-d))
    lrd[r-1].append((l-1,+d))

def BFD(x):
    global checked,answer,lrd
    checked[x]=1
    #print("x>>>",x,lrd[x])
    for llrrdd in lrd[x]:
        #print(llrrdd,x)
        item=llrrdd[0]
        if answer[item]=="first":
            answer[item]=answer[x]-llrrdd[1]
        else:
            if answer[item]!=answer[x]-llrrdd[1]:
                print("No")
                exit()
        if checked[item]==0:
            BFD(item)

checked=[0]*n
answer = ["first"]*n

for i in range(n):
    if checked[i]==0:
        answer[i]=1
        BFD(i)

print("Yes")
