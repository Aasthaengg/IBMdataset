n, k = map(int, input().split())
s = input()
for c in range(n):
  if c == k-1:
    print(s[c].lower(), end="")
  else:
    print(s[c], end="")