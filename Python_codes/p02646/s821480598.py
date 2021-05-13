a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if a<b:
  if w<v:
    if (v-w)*t>=(b-a):
      print("YES")
    else:
      print("NO")
  else:
    print("NO")
else:
  if w<v:
    if (v-w)*t>=(a-b):
      print("YES")
    else:
      print("NO")
  else:
    print("NO")