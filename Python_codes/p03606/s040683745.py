n=int(input())
t=0
for i in range(n):
  x,y=map(int, input().split())
  t+=y-x+1
print(t)