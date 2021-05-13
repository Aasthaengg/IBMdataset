n = int(input())
a = list(map(int, input().split()))
sa = sorted(a)
r = []
# ruiseki
su = 0
for i in range(n):
  su += sa[i]
  r.append(su)
ans = 1

for i in range(n-1):
  if (r[~i-1]*2 >= sa[~i]):
    ans += 1
  else:
    break
print(ans)