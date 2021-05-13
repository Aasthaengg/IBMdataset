ch = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
      'n','o','p','q','r','s','t','u','v','w','x','y','z']

n = int(input())

import queue
q=queue.Queue()
l = 1
q.put(["a", 0])

while True:
  temp = q.get()
  l=len(temp[0])
  if l==n:
    break
    
  for i in range(temp[1]+2):
    ne = temp[0]+ch[i]
    nn = max(temp[1], i)
    q.put([ne, nn])

print(temp[0])
while not q.empty():
  print(q.get()[0])
  
