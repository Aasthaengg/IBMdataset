# coding: utf-8
# Your code here!
from collections import deque
s=deque(input())
Q=int(input())
count=0
query=[]
for i in range(Q):
    arr=input().split()
    query.append(arr)

for i in range(Q):
    if query[i][0]=="1":
        count+=1
    else:
        if count%2==0:
            if query[i][1]=="1":
                s.appendleft(query[i][2])
            else:
                s.append(query[i][2])
        else:
            if query[i][1]=="1":
                s.append(query[i][2])
            else:
                s.appendleft(query[i][2])
if count%2==0:
    for i in range(len(s)):
        print(s[i],end="")
        
else:
    s.reverse()
    for i in range(len(s)):
        print(s[i],end="")