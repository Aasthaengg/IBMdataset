n, q = map(int, input().split())
s = input()
ans = [0]
for i in range(1, n):
  if s[i - 1:i + 1] == "AC":
    ans.append(ans[-1] + 1)
  else:
    ans.append(ans[-1])
for _ in range(q):
  l, r = map(int, input().split())
  print(ans[r - 1] - ans[l - 1])