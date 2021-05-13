from collections import deque
A=[deque(list(input())) for _ in range(3)]

num=0
while 1:
    if len(A[num])==0:
        if num==0:print("A")
        elif num==1:print("B")
        else:print("C")
        exit()
    else:
        word=A[num].popleft()
        if word=="a":num=0
        elif word=="b":num=1
        else:num=2