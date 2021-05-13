n=int(input())
p=list(map(int, input().split()))
q=list(map(int, input().split()))
ans = sum(p)+q[n-1]
tmp = ans
for i in range(n-1):
  tmp = tmp + q[n-i-2] - p[n-i-1]
  ans = max(ans, tmp)
print(ans)