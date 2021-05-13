t = input()
a = input().split()
a = [int(i) for i in a]
ans = "APPROVED"
for i in range(len(a)):
  if a[i] % 2 == 0:
    if a[i] % 3 == 0 or a[i] % 5 == 0:
      continue
    else:
      ans = "DENIED"
      break
  else:
    continue
print(ans)