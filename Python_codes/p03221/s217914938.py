import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append([])

for i in range(m):
    p,y=map(int,input().split())
    lst[p-1].append([i,p,y])

for i in range(n):
    lst[i]=sorted(lst[i],key=lambda x:x[2])

for i in range(n):
    for j in range(len(lst[i])):
        lst[i][j].append(j+1)

lst=[i for j in lst for i in j]
lst=sorted(lst,key=lambda x:x[0])

for i in range(m):
    left=str(lst[i][1])
    right=str(lst[i][3])
    prnt=["0"*(6-len(left)),left,"0"*(6-len(right)),right]
    print("".join(prnt))