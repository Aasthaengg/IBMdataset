N = int(input())
ans = 0
b = 380000.0
for i in range(N):
  s = list(input().split())
  if s[1] == "JPY":
    ans += int(s[0])
  else:
    ans += float(s[0]) * b
print(ans)