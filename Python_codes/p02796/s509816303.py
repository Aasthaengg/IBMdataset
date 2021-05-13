N = int(input())

R = []
for i in range(N):
  x, l = map(int, input().split(" "))
  R.append([x-l, x+l])
R.sort(key=lambda x: x[1])
ans = 1
length = R[0][1]
for r in R:
  if length <= r[0]:
    ans += 1
    length = r[1]

print(ans)