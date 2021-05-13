from collections import deque
N=int(input())
b=list(map(int,input().split()))
flag=0
op=deque()
#1→12→122→1232→11232→121232→1221232→11221232→111221232
#print(b)
while len(b)>0:
    for i in range(len(b)-1,-1,-1):
        if b[i]==i+1:
            #print(b[i])
            op.appendleft(b.pop(i))
            flag=1
            break
    if flag==0:
        break
    flag=0
    #print(op,b)
#print(op)
if len(b)==0:
    for i in range(N):
        print(op.popleft())
else:
    print("-1")
