l = list(map(int,input().split()))
n = int(input())
l.sort()
for i in range(n):
  l[2] = l[2] * 2
  
print(l[0]+l[1]+l[2])