n = int(input())
a = [int(k) for k in input().split()]
ans = 0
for i in a:
  ans += 1/i
print(1/ans)