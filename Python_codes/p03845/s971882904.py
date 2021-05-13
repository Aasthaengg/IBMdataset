n = int(input())
t = list(map(int,input().split()))
m = int(input())
px = [0]*m

for i in range(0,m):
  px[i] = input().split()
  
x = []
#print(px)
tmp = [0]*m

for i in range(0,m):
  tmp = t[:]
  #temp = t[int(px[i][0])-1]
  tmp[int(px[i][0])-1] = int(px[i][1])
  #print(tmp)
  #t[int(px[i][0])-1] = temp
  x.append(sum(tmp))
  
#print(x)

for i in x:
  print(i)
