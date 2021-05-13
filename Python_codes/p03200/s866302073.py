S = input()
N = len(S)
cnt = 0
ans = 0
for c in S[::-1]:
  if c == 'W':
    cnt += 1
  else:
    ans += cnt

print(ans)
