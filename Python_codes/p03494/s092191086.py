def irritation(n):
  ans = 0
  while n % 2==0:
    n /= 2
    ans += 1
  return ans

n = int(input())
a = map(int, input().split())
ans = min(map(irritation, a))

print(ans)