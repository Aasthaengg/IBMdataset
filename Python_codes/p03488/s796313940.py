from sys import exit
from itertools import groupby

s=input()
x,y=map(int,input().split())

s=[[h, len(list(g))] for h, g in groupby(s)]
a,b=[],[]
turn=True
#初めまっすぐの場合
if s[0][0]=="F":
    x-=s[0][1]
    s.pop(0)
for i in s:
    if i[0]=="F":
        if turn:
            a.append(i[1])
        else:
            b.append(i[1])
    elif i[1]%2==1:
        turn=not turn
a.sort(reverse=True)
b.sort(reverse=True)
for i in a:
    x=abs(x)-abs(i)
if x!=0:
    print("No")
    exit()
for i in b:
    y=abs(y)-abs(i)
if y!=0:
    print("No")
    exit()
print("Yes")
