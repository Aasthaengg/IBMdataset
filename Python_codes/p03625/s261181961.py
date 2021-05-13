from collections import *
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(int)
for i in l:
    d[i]+=1
x=[]
for i in d:
    if(d[i]>=4):
        x.append(i)
        x.append(i)
    elif(d[i]>=2):
        x.append(i)
x.sort(reverse=True)
if(len(x)<2):
    print(0)
else:
    print(x[0]*x[1])