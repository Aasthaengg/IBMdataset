n = int(input())
a = list(map(int, input().split()))

ans = "APPROVED"
for x in a:
  if (x % 2 == 0):
    if (x % 3 != 0 and x % 5 != 0):
      ans = "DENIED"
print(ans)