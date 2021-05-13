h,w=map(int,input().split())
a=[]

from collections import deque
fifo = deque()
a.append(["@"]*(w+2))
for i in range(h):
    s=input()
    temp=["@"]
    for j in range(w):
        if s[j]=="#":
            fifo.append([i+1,j+1])
            temp.append(0)
        else:
            temp.append(s[j])
    temp.append("@")
    a.append(temp)
a.append(["@"]*(w+2))

result=0
#print(a)

while len(fifo)>0:
    temp=fifo.popleft()
    y,x=temp[0],temp[1]

    for item in [[0,1],[1,0],[-1,0],[0,-1]]:
        #print(y+item[0],x+item[1])
        if a[y+item[0]][x+item[1]]==".":
            fifo.append([y+item[0],x+item[1]])
            a[y+item[0]][x+item[1]]=a[y][x]+1
            result=max(result,a[y+item[0]][x+item[1]])
    
print(result)

    

