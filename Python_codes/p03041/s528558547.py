n, k = map(int, input().split())
s = input()

k -= 1

for i in range(n):
  print(s[i] if i != k else s[i].lower(), end="")