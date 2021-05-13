n = int(input())
nums = map(int, input().split())
ok = True
for num in nums:
  if (num % 2 == 0):
    if (num % 3 != 0 and num % 5 != 0):
      ok = False

if(ok):
  print("APPROVED")
else:
  print("DENIED")