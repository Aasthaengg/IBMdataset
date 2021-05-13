N = int(input())
a = [int(_) for _ in input().split()]
a.append(0)
cnt = 1
ans = 0
for i in range(N):
  if a[i+1] == a[i]:
    cnt += 1
  else:
    ans += cnt // 2
    cnt = 1
print(ans)