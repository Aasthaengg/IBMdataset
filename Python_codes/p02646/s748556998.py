a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
dist = abs(a-b)
velo = v-w
if dist > velo*t:
  print("NO")
else:
  print("YES")