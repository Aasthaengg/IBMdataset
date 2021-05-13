num = list(map(int, input().split()))
num.sort()

x = num[2] * 3 - sum(num)

if x%2 == 0:
  ans = int(x/2)
else:
  ans = int(x//2 + 2)

print(ans)
