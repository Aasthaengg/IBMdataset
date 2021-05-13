a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

#距離
l = abs(a-b) 

#差分
diff = t*(v-w)

if l > diff:
  print("NO")
else:
  print("YES")