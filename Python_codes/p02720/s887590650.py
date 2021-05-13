K=int(input())
import queue
q = queue.Queue()
for i in range(1,10):
  q.put(i)
for i in range(K-1):
  a=q.get()
  if a%10!=0:
    q.put(10*a+(a%10)-1)
  q.put(10*a+(a%10))
  if a%10!=9:
    q.put(10*a+(a%10)+1)
print(q.get())