n = int(input())
X = [0]*n
Y = [0]*n
for i in range(n):
  X[i],Y[i] = map(int,input().split())  
  
dic = {}
for i in range(n):
  for j in range(n):
    if i!=j:
      x = X[i]-X[j]
      y = Y[i]-Y[j]
      dic[(x,y)] = dic.get((x,y),0) + 1

if n == 1:
  print(1)
else:  
  print(n-max(dic.values()))