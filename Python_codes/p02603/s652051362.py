n = int(input())
a = [int(x) for x in input().split()]

ans = 1000

for i in range(n-1):
  ans += (ans//a[i])*max(0, (a[i+1]-a[i]))

print(ans)