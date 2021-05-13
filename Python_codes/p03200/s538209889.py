s = input()
ans = 0
count = 0
w_count = 0
for i in s:
  if i == "W":
    ans += count - w_count
    w_count += 1
  count += 1
print(ans)