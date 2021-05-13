L, R = map(int, input().split())
  
if R - L >= 2018:
  print(0)
  exit()
  
lst = []
for i in range(L,R+1):
  lst.append(i%2019)
  
lst.sort()

if lst[0] == 0:
  print(0)
  exit()
  
rlt = 2020
for i in range(len(lst)):
  for j in range(i+1,len(lst)):
    rlt = min(rlt, (lst[i]*lst[j])%2019)
    
print(rlt)