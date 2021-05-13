from collections import deque
 
n=int(input())
command=[0 for i in range(n)]
k=[0 for i in range(n)]
k_queue= deque([])
 
for i in range(n):
    s=input()
    if s=="deleteFirst" or s=="deleteLast":
        command[i],k[i]=s,0
    else:
        command[i],k[i]=s.split()
     
for i in range(n):
    if command[i]=="insert":
        k_queue.appendleft(k[i])
    elif command[i]=="deleteFirst":
        k_queue.popleft()
    elif command[i]=="deleteLast":
        k_queue.pop()
    else:
        try: k_queue.remove(k[i])
        except ValueError: y=0
print( " ".join(map(str, k_queue)))
