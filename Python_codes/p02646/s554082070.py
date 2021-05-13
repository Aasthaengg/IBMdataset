a,v=map(int,input().split())
b,w=map(int,input().split())
s=int(input())
if(abs(a-b)>(v-w)*s):
  print("NO")
else:
  print("YES")