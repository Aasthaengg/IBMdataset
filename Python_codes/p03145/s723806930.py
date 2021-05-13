a,b,c = list(map(int, input().split()))
m = max(a,b,c)

if m ==a:
  ans = b*c/2
elif m ==b:
  ans = a*c/2
elif m ==c:
  ans = a*b/2

print(int(ans))