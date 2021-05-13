stack=[]
n=int(input())
color=[]
graph={}
d_time=[]
f_time=[]
time=0
root=[i for i in range(1,n+1)]

for i in range(n):
    tmp=list(map(int,input().split()))
    graph[tmp[0]]=[0 for j in range(n+1)]
    color=["white" for l in range(n+1)]
    d_time=[0 for j in range(n+1)]
    f_time=[0 for j in range(n+1)]
    for k in range(tmp[1]):
        graph[tmp[0]][tmp[2+k]]=1
        if tmp[2+k] in root:
            root.remove(tmp[2+k])

def function(number):
    global time
    stack.append(number)
    color[number]="gray"
    time+=1
    d_time[number]=time
    while stack!=[]:
        u=stack[-1]
        if 1 in graph[u]:
            v=graph[u].index(1)
            graph[u][v]=0
            if color[v]=="white":
                color[v]="gray"
                time+=1
                d_time[v]=time
                stack.append(v)
        else:
            stack.pop()
            color[u]="black"
            time+=1
            f_time[u]=time

if root==[]:
    function(1)
else:
    for i in range(len(root)):
        function(root[i])

for i in range(1,n+1):
    print(i,d_time[i],f_time[i])
