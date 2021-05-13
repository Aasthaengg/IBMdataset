n, m = map(int, input().split())
 
forbidden = []
for i in range(m):
  forbidden.append(int(input()))
forbidden = set(forbidden) 
ans = [0]*(n+1)
ans[0] = 1
if 1 not in forbidden:
  ans[1] = 1
for i in range(2,n+1):
  if i not in forbidden:
    ans[i] += ans[i - 1] + ans[i - 2]
    ans[i] %= 1000000007
print(ans[-1])