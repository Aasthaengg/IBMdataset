a, b, k = map(int, input().split())
m = b if a > b else a
ans = []
for i in range(1, m+1):
  if a % i == 0 and b % i == 0:
    ans.append(i)
print(ans[-k])