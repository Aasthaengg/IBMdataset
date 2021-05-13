s, c = map(int, input().split())

count = 0
if s*2 <= c:
  count = s
  c = c - 2*s
  count += c//4
else:
  count = c//2
print(count)