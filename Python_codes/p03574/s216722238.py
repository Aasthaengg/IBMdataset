import numpy as np
h,w = (map(int,input().split(' ')))
x = []
for i in range(h):
  x.append(input())
  
y = np.zeros((h,w),dtype=int)
#print(y)           
for n,i in enumerate(x):
  for j in range(w):
    if i[j] == '#':
#同列
      if j >= 1:
        if x[n][j-1] != '#':
          y[n][j-1]  +=1  
      if j < w-1:
        if x[n][j+1] != '#':
   	        y[n][j+1]  +=1  
#前列 
      if n > 0:
        if x[n-1][j] !='#':
          y[n-1][j] +=1
        if j >= 1:
          if x[n-1][j-1] !='#':
            y[n-1][j-1] +=1
        if j < w-1:
          if x[n-1][j+1] !='#':
            y[n-1][j+1] +=1
#後列
      if n < h-1:
        if x[n+1][j] != '#':  
          y[n+1][j] +=1
        if j >= 1:
          if x[n+1][j-1] != '#':
            y[n+1][j-1] +=1
        if j < w-1:
          if x[n+1][j+1] != '#':
            y[n+1][j+1] +=1

y2 = y.astype(np.unicode)
            
for n,i in enumerate(x):
  for n2,j in enumerate(i):
    if j == '#':
      y2[n][n2] ='#'
  print(''.join(list(y2[n])))  
  
