N = int(input())
p = list(map(int, input().split()))
ans = 0
i = 0
while i < N - 1:
  if i < N - 4 and p[i] == i + 1 and p[i + 1] == i + 2 and p[i + 2] == i + 3 and p[i + 3] == i + 4:
    temp = p[i]
    p[i] = p[i + 1]
    p[i + 1] = temp
    temp = p[i + 2]
    p[i + 2] = p[i + 3]
    p[i + 3] = temp
    i += 3
    ans += 2
    continue
  if p[i] == i + 1:
    temp = p[i]
    p[i] = p[i + 1]
    p[i + 1] = temp
    ans += 1
  i += 1
if p[N - 1] == N:
  ans += 1
print(ans)