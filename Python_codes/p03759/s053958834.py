a,b,c = map(int,input().split())
dis_a = b-a
dis_b = c-b
if dis_a == dis_b:
  print("YES")
else:
  print("NO")