S = input()
K = int(input())

ans = -1
for s in S[:K]:
  x = int(s)
  if x != 1:
    ans = x
    break
else:
  ans = 1

print(ans)
