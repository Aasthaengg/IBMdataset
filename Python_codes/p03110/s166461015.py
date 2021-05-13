n = int(input())
ans = 0
for _ in range(n):
  i = input().split()
  if i[1] == 'JPY':
    ans += int(i[0])
  else:
    ans += float(i[0]) * 380000
print(ans)