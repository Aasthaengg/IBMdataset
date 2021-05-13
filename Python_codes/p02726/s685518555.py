n,x,y = map(int,input().split())
ko = [0 for i in range(10**4)]
for i in range(1,n):
  for j in range(i+1,n+1):
    c1 = j-i
    c2 = abs(x-i)+1+abs(y-j)
    ko[min(c1,c2)] += 1
  #  print(i,j,j-i,c1,c2,ko[:10])
for i in range(1,n):
  print(ko[i])