from sys import exit
s=input()
x,y=map(int,input().split())

t=[[s[0],1]]
for i in range(1,len(s)):
    if t[-1][0]==s[i]:
        t[-1][1]+=1
    else:
        t.append([s[i],1])

a,b=[],[]
turn=True
#初めまっすぐの場合
if t[0][0]=="F":
    x-=t[0][1]
    t.pop(0)
for i in t:
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
