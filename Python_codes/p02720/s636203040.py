import queue

k = int(input())

q = queue.Queue()

for i in range(9):
  q.put(i+1)
  
for i in range(k):
  ans = q.get()
  if ans%10 != 0:
    q.put(10*ans+ans%10-1)
  q.put(10*ans+ans%10)
  if ans%10 != 9:
    q.put(10*ans+ans%10+1)
    
print(ans)
  
