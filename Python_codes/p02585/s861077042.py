n, k = list(map(int,input().split()))
jump = list(map(int,input().split()))
arr = list(map(int,input().split()))
best = - (10**28)
VV = []
 
for i in range(n):
  if i not in VV:
    order = []
    prev_pos = i
    visited = []
    sub_best = 0
    order = []
    l = 0
 
    for jjj in range(n):
      order.append(arr[prev_pos])
      #sub_best = max(sub_best, sum(order))
      visited.append(prev_pos)
      VV.append(prev_pos)
      l += 1
 
      next_pos = jump[prev_pos] - 1
      prev_pos = next_pos
      if next_pos in visited:
        break
 
    if sum(order)<1:
      limit = min(k,l*2)
      ss = 0
    else:
      limit = (k % l) + l
      limit = min(k,limit)
      ss = sum(order) * ((k//l) - 1)
      ss = max(ss,0) 
 
    sub_best = ss
   # print(limit, order, ss, sub_best)
    
    order = order + order + order
    
    for chuj in range(1,limit+1):
      kk = sum(order[0:0+chuj])
      best = max(best, sub_best + kk)
      for op in range(len(order)-chuj):
        kk -= order[op]
        kk += order[op+chuj]
        best = max(best, sub_best + kk)
      
print(best)