ans = "No"
a, b, c = [ int(v) for v in input().split() ]
if a + b >= c:
  ans = "Yes"
print(ans)