from collections import deque

SA=input()
SB=input()
SC=input()

da=deque()
db=deque()
dc=deque()

for i in range(len(SA)):
    da.append(SA[i])
for i in range(len(SB)):
    db.append(SB[i])
for i in range(len(SC)):
    dc.append(SC[i])


nv="a"
while len(da)>=0 and len(db)>=0 and len(dc)>=0:
    if nv =="a" and len(da)>0:
        nv = da.popleft()
    elif nv =="a":
        print("A")
        exit()
    elif nv =="b" and len(db)>0:
        nv = db.popleft()
    elif nv =="b":
        print("B")
        exit()    
    elif nv =="c" and len(dc)>0: 
        nv = dc.popleft()
    elif nv =="c":
        print("C")
        exit()

