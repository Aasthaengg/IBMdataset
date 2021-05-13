a, b, c = map(int,(input().split()))
ans = "NO"
if a-b == b-c or b-a == c-b:
  ans = "YES"
print(ans)