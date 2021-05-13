a, b, k  = map(int, input().split())
c = 0
ans = []
if a > b:
  c = b
else:
  c = a

for i in range(1, c+1):
  if a % i == 0 and b % i == 0:
    ans.append(i)
  else:
    continue


print(ans[-k])