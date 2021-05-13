from collections import deque
 
O=input()
E=input()
 
o=deque(O)
e=deque(E)
 
s=''
while True:
  if not e  and not o:
    break
  if o:
    s+=o.popleft()
  if e:
    s+=e.popleft()
    
  
print(s)