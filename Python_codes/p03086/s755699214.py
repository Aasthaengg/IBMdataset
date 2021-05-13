s = input()
count = 0
ans = 0
for i in s:
  if i == "A" or i == "C" or i == "G" or i == "T":
    count += 1
  else:
    count = 0
  if count > ans:
    ans = count
print(ans)