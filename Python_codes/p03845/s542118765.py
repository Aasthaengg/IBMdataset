n = int(input())
l = list(map(int,input().split()))
s = sum(l)
m = int(input())

for i in range(m):
  x,y = map(int, input().split())
  print(s - l[x-1]+y)

  
 