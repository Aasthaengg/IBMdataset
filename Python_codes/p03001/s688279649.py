W, H, x, y = map(int,input().split())

s = W*H/2
print(s)

if x*2 == W and y*2 == H:
  print("1")
else:
  print("0")