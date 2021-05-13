# coding: utf-8
# Your code here!
import copy

def minus(num):
    for i in range(N):
        eva[i][num]*=(-1)
    return 0

N,M=map(int,input().split())

eva=[]
for _ in range(N):
    x,y,z=map(int,input().split())
    eva.append([x,y,z])
    

ans=[]
for _ in range(2):
    minus(0)
    for __ in range(2):
        minus(1)
        for ___ in range(2):
            minus(2)
            eva.sort(key=lambda x:sum(x),reverse=True)
            #print(eva)
            temp=copy.deepcopy(eva[:M])
            ans.append(temp)
            #print(ans)
            
shin=0
for item in ans:
    temp=0
    for comp in item:
        temp+=sum(comp)
        
    shin=max(temp,shin)
    
print(shin)