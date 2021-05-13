N = int(input())
list_FF = []

for i in range(N):
  list_F = list(map(int, input().split()))
  list_FF.append(list_F)

list_PP = []

for i in range(N):
  list_P = list(map(int, input().split()))
  list_PP.append(list_P)  
  
count = 1
quota = 0

for i in range(N):
  quota+= list_PP[i][list_FF[i].count(1)]

maxquota = quota
    
while count < 2** 10:
  l = list(bin(count))
  lc_tdc = l[2:]
  l_tdc = []
  while lc_tdc:
    l_tdc.append(int(lc_tdc.pop(0)))
  
  while len(l_tdc) < 10:
    l_tdc.insert(0, 0)

  quota = 0
  
  for i in range(N):
    corresp = 0
    for j in range(10):
      corresp+= l_tdc[j]* list_FF[i][j]
    quota+= list_PP[i][corresp]
  maxquota = max(quota, maxquota)
      
  count+= 1

print(maxquota)