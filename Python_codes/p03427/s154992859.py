s = input()
n = len(s)

ans = 0
if s[1:] == '9' * (n - 1):
  ans = int(s[0]) + 9 * (n - 1)
elif n != 1:
  ans = int(s[0]) + 9 * (n - 1) - 1
else:
  ans = int(s[0])

print(ans)
