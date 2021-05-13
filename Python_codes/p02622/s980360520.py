line1 = input()
line2 = input()
ans = 0
for i in range(len(line1)):
  if line1[i] != line2[i]:
    ans += 1
print(ans)
