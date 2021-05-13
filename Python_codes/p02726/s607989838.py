n,x,y = map(int,input().split())
ko = [0 for i in range(10**4)]
for i in range(1,n):
  for j in range(i+1,n+1):
    c1 = j-i
    if i<=x and y<=j:
      c2 = (x-i)+1+(j-y)
    elif i<=x and j<y:
      c2 = (x-i)+1+(y-j)
    elif x<i and y<=j:
      c2 = (i-x)+1+(j-y)
    else:
      c2 = (i-x)+1+(y-j)
    ko[min(c1,c2)] += 1
  #  print(i,j,j-i,c1,c2,ko[:10])
for i in range(1,n):
  print(ko[i])