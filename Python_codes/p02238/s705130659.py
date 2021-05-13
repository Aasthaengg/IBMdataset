#coding:utf-8
from copy import deepcopy

n = int(input())
c = ["white" for i in range(n)]
d = [0 for i in range(n)]
f = [0 for i in range(n)]
S = []
class DFS:
    def __init__(self, key, color="white",nex=None):
        self.color = color
        self.nex = nex
        self.key = key

objList = [DFS(i+1) for i in range(n)]
for i in range(n):
    data = list(map(int,input().split()))
    times = data[1]
    obj = objList[i]
    for j in range(times):
        index = data[2+j] - 1
        nextobj = DFS(index+1)
        obj.nex = nextobj
        obj = obj.nex


time = 1
def check(first,time):
    obj = objList[first]
    c[first] = "gray"
    d[first] = time
    f[first] = time
    S.append(first+1)
    
    while S != []:
        index = S[-1] - 1
        u = objList[index]
        v = u.nex
    
        if v != None:
            objList[index] = v
            if c[v.key - 1] == "white":
                index = v.key - 1
                v = objList[index]
                c[v.key-1] = "gray"
                time += 1
                d[index] = time
                S.append(v.key)

           
                
        else:
            S.pop()
            c[u.key-1] = "black"
            time += 1
            f[index] = time
    return time


for i in range(n):
    if f[i] == 0:
        time = check(i,time) + 1
        

k = 1
for i,j in zip(d,f):
    print(k,i,j)
    k += 1
