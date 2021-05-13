
w, h ,x, y = list(map(int, input().split()))
ans = str(w*h/2)
if x == w/2 and y == h/2:
  ans2 = "1"
else:
  ans2 = "0"
  
print(ans+" "+ans2)
