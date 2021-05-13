import sys
sys.setrecursionlimit(10000000)
n,u,v=map(int,input().split())
kilist=[[] for i in range(n)]
for i in range(n-1):
        a,b=map(int,input().split())
        kilist[a-1].append((b,1))
        kilist[b-1].append((a,1))    
visitedlist=[-1 for  _ in range(n)]
anslist=[0 for _ in range(n)]
searchedlist=[-1 for _ in range(n)]        
def search(i):
        searchedlist[i-1]=1
        visitedlist[i-1]=1
        flag=0
        for j in kilist[i-1]:
            if visitedlist[j[0]-1]<0:
                visitedlist[j[0]-1]=1
                flag+=1
                anslist[j[0]-1]=anslist[i-1]+j[1]
        else:
            pass
        if flag>0:    
            for k in kilist[i-1]:
                if searchedlist[k[0]-1]==-1:
                    search(k[0])
search(u)
u_list=anslist.copy()
visitedlist=[-1 for  _ in range(n)]
anslist=[0 for _ in range(n)]
searchedlist=[-1 for _ in range(n)]  

q=search(v)
v_list=anslist.copy()

maxi=0
for i in range(n):
    if u_list[i]<=v_list[i]:
        maxi=max(maxi,v_list[i])
print(maxi-1)