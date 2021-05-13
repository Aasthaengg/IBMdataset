n = input()
hs = list(map(int,input().split(" ")))

step = 0
while(True):
  
  if(sum(hs) == 0):
    break
  
  start = None
  stop = None
  
  for i,h in enumerate(hs):

    if(h>0 and start is None):
      start = i
    if(h==0 and start is not None and stop is None):
      stop = i
     	
  if(start is not None and stop is None):
    stop = len(hs)
    
  for i in range(start, stop):
    hs[i] -= 1
    
  step += 1
  
print(step)