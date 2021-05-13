# coding: utf-8
# Your code here!
N=int(input())

P=[]
for _ in range(N):
    P.append(int(input())-1)
    
#print(P)

root=[-1]*N
count=[0]*N
for item in P:
    if item == 0:
        root[item]=item
        count[root[item]]+=1
        continue
    if root[item-1]==-1:
        root[item]=item
        count[root[item]]+=1
    else:
        root[item]=root[item-1]
        count[root[item]]+=1
"""
print(root)
print(count)
print("===========================")
"""
print(N-max(count))
