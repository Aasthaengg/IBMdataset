N = int(input())

ans = "No"

for x in range(1,10):
  for y in range(1,10):
    if N == x*y:
      ans = "Yes"
      break
print(ans)