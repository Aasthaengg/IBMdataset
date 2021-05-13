W,a,b=list(map(int, input().split()))
ar=a+W
br=b+W
if 0 <= ar-b <= W or 0 <= br-a <=W:
  print(0)
else:
  print(min(abs(br-a), abs(ar-b)))