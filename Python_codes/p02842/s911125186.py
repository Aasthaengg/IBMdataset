n = int(input())
ans = int(n / 1.08)
if int(ans * 1.08) != n:
  ans = int(n / 1.08) + 1
  if (int(ans * 1.08)) != n:
    ans = ':('
print(ans)