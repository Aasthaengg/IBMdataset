S = list(input())
k = int(input())

ans = ''
for i, s in enumerate(S):
  if i%k == 0:
    ans += s
print(ans)