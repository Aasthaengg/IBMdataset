a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
d1=abs(a-b)
d2=(v-w)*t
if d1<=d2:
  print("YES")
else:
  print("NO")
