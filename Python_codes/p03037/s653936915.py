n,m = map(int, input().split())
x = [0]*n
a = 0
l  =[0]*m
r = [0]*m
for i in range(m):
  l[i],r[i]=map(int,input().split())
a = min(r)-max(l)+1
print(max(0,a))