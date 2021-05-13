a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
gap=abs(a-b) 
if v>w:
  c=(v-w)*t
  if gap<=c:
    print('YES')
  else:
    print('NO')
else:
  print('NO')
