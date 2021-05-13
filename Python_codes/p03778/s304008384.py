w,a,b = [int(i) for i in input().split()]
ans = 0
if a <= b <= a+w or b <= a <= b+w:
  print(ans)
else:
  ans = min(abs(b-a-w),abs(a-b-w))
  print(ans)