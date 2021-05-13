w,h,x,y = map(int, input().split())

if w%2 == 0 and h%2 == 0 and  x == w//2 and y == h//2:
  print(w*h/2 , 1)
else:
  print(w*h/2, 0)
