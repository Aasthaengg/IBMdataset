K, X = map(int, input().split())
s = ""
for i in range(max(X-K+1, -1000000), min(X+K-1, 1000000)+1):
  s += " "
  s += str(i)
print(s[1:])