import math
N, M = map(int, input().split())
nums = list(map(int, input().split()))
lcm = 1
b_cnt = -1
for num in nums:
  lcm = lcm*(num//2)//math.gcd(lcm, num//2)
  count = 0
  while num%2 == 0:
    count += 1
    num //= 2
  if b_cnt < 0:
    b_cnt = count
  elif count != b_cnt:
    print(0)
    exit()
print((M+lcm)//(lcm*2))