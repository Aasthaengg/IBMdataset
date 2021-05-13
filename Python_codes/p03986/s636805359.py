X = input()
N = len(X)
cnt = 0
ans = 0
for x in X:
  if x == "S":
    cnt += 1
  else:
    if cnt == 0:
      ans += 1
    else:
      cnt -= 1

print(ans * 2)