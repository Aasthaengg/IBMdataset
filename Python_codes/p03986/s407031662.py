A=list(input())
from collections import deque
que=deque()
for i in A:
   if i=="T":
      if que==deque():
         que.append("T")
      elif que[-1]=="T":
         que.append("T")
      else:
         que.pop()
   else:
      que.append("S")
print(len(que))