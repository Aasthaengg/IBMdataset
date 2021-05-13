ans = []

for _ in range(4):
  ans.append(int(input()))

print(min(ans[:2]) + min(ans[2:]))