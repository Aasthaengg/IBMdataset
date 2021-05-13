n = int(input())
aa =list(map(int, input().split()))

list1 =[0] * n
cnt = 1  
for i in range(n-1):
  if aa[i+1] > aa[i]:
    list1[i+1] = 1
  elif aa[i+1] < aa[i]:
    list1[i+1] = -1
  elif aa[i+1] == aa[i]:    
    list1[i+1] = 0

while 1 in list1 and -1 in list1:
  del list1[:max(list1.index(1), list1.index(-1))]
  list1[0] = 0
  cnt += 1
  
print(cnt)
