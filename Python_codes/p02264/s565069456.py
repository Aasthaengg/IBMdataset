from collections import deque

n , q = map(int,input().split())
p , t = deque() , deque()
for i in range(n):
    x , y = input().split()
    p.append(x)
    t.append(int(y))
time = 0
temp1 = ""
temp2 = 0

while p:
    temp1 , temp2 = p.popleft() , t.popleft()
    if temp2 <= q :
        time += temp2
        print(temp1,time)
        temp1 , tmep2 = "" , 0
    else:
        time += q
        temp2 -= q
        p.append(temp1)
        t.append(temp2)