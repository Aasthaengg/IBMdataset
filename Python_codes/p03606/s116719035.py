N = int(input())
ans = 0
for i in range(N):
  l,r = [int(x) for x in input().split()]
  ans +=r-l+1
print(ans)