from collections import deque

n,q=[int(i) for i in input().split()]
name=[0 for i in range(n)]
time=[0 for i in range(n)]
answer_name=[]
answer_time=[]
total_time=0

for i in range(n):
    name[i],time[i]=input().split()

d_name = deque(name)
d_time = deque(time)

while len(d_name)>0:

    a=d_name.popleft()
    b=int(d_time.popleft())

    if b>q:
        d_name.append(a)
        d_time.append(b-q)
        total_time=total_time+q

    else:
        total_time=total_time+b
        answer_name.append(a)
        answer_time.append(total_time)

for i in range(len(answer_time)):
    print(answer_name[i], answer_time[i])

