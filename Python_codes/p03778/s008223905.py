w,a,b = map(int, input().split())

if a<=b<=a+w:
  print(0)
  exit()
if b<=a<=b+w:
  print(0)
  exit()

ans1=b-a-w
ans2=a-b-w

print(min(abs(ans1),abs(ans2)))