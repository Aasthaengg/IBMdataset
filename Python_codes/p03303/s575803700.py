s = input()
w = int(input())
ans = ''
for i, x in enumerate(s):
  if i%w == 0:
    ans += x
print(ans)