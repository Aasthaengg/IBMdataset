n,k,l=map(int,input().split())

data=[[] for i in range(n+1)]
for i in range(k):
    p,q=map(int,input().split())
    data[p].append(q)
    data[q].append(p)
parent=[0]*(n+1)
num=1
for i in range(1,n+1):
    if parent[i]==0:
        parent[i]=num
        que=[i]
        while que:
            h=que.pop()
            for u in data[h]:
                if parent[u]==0:
                    parent[u]=num
                    que.append(u)
        num+=1

data=[[] for i in range(n+1)]
for i in range(l):
    r,s=map(int,input().split())
    data[r].append(s)
    data[s].append(r)
flag=[0]*(n+1)
num=1
for i in range(1,n+1):
    if flag[i]==0:
        flag[i]=num
        que=[i]
        while que:
            h=que.pop()
            for u in data[h]:
                if flag[u]==0:
                    flag[u]=num
                    que.append(u)
        num+=1

lst=[]
for i in range(1,n+1):
    lst.append([parent[i],flag[i],i])

ans=[1]*(n+1)
lst.sort()
k=0
for i in range(1,n):
    if lst[i][:2]==lst[i-1][:2]:
        k+=1
    else:
        for j in range(i-1-k,i):
            ans[lst[j][2]]+=k
        k=0
for j in range(n-1-k,n):
    ans[lst[j][2]]+=k
print(*ans[1:])