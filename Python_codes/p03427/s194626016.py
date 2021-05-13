s = input()
n = len(s)

ans = int(s[0]) + 9 * (n - 1)

if n != 1:
  if s[1:] != '9' * (n-1):
    ans -= 1

print(ans)
