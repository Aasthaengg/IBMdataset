from collections import deque
N = int(input())
a = deque()
a_num = 0
b =deque()
c = deque()
for i in range(N):
  a_num = int(input())
  a.append(a_num)
  k,p=0,0
  x = [0]*N
  b_num=deque()
  for i in range(a_num):
    k,p = map(int,input().split())
    b_num.append(k-1)
    x[k-1]=p
  b.append(b_num)
  c.append(x)
max_num = 0   
for i in range(2**N):
  two = format(i,"015b")
  two = two[::-1]
  flag=True
  for i,k in enumerate(two):
    if flag == False:
      break
    if i<N:
      if k =="1":
        for l in range(a[i]):
          for j in b[i]:
            #print(b[i],c[i][j],two[j])
            if c[i][j]!=int(two[j]):
              flag =False
              break
          if flag ==False:
            break
        if flag == False:
          break
    
    else:
      break
  if flag == True:
    #print(two)
    max_num = max(max_num,two.count("1"))  
print(max_num)