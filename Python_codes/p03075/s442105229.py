a = [int(input()) for i in range(5)]
k = int(input())
ans = "Yay!"
for ai in a:
  for aj in a:
    if ai-aj > k:
      ans = ":("
print(ans)