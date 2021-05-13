n = int(input())
b = list(map(int,input().split()))
ans = [0]*n
for i in range(n-1):
  if i == 0:
    ans[i] = b[i]
  else:
    ans[i] = min(b[i-1],b[i])
print(sum(ans)+b[-1])