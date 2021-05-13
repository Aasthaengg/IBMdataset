import sys
n = int(input())
ans = [0]*(n+1) #ans[k]:入力値kでの答え
#初期値３、４、５
if n == 1 or n == 2:
  print(0)
  sys.exit()
  
if 3<= n <=5:
  print(1)
  sys.exit()
  
  
ans[3] = 1
ans[4] = 1
ans[5] = 1
  
for i in range(6,n+1):
  start = 3
  stop = i-3
  s = 1
  for j in range(start,stop+1):
    s = (s+ans[j]) % (10**9+7)
    
  ans[i] = s
  
print(ans[-1])  