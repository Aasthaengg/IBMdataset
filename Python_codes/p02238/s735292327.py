# coding: utf-8
def depth(i, adj, Dep, Arr, times):
    if Dep[i-1]:
        return times
    Dep[i-1]=times
    times+=1
    # t=[depth(j, adj, Dep, f, times) j in adj[i-1]]
    for j in adj[i-1]:
        times=depth(j, adj, Dep, Arr, times)
    Arr[i - 1]=times
    times+=1
    return times


n=int(input())
adj=[list(map(int, input().split()))[2:] for i in range(n)]

d,f=[0]*n,[0]*n

t=1

dlist=[i for i in range(n) if d[i]==0]

for i in dlist:
    t = depth(i + 1, adj, d, f, t)

for i, df in enumerate(zip(d, f)):
    print(i + 1, *df)