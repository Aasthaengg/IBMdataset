n = int(input())
d,x = map(int, input().split())
a = [int(input()) for _ in range(n)]
c = 1
ans = x
for i in a:
  for j in range(1, d+1):
    if i*j+1 <= d:
      c += 1
    else:
      ans += c
      c = 1
      break
print(ans)