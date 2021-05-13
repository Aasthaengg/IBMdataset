a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
f = (v-w)*t
c = a-b
if(c<0):
  c *= (-1)
if(c>f):
  print("NO")
else:
  print("YES")

