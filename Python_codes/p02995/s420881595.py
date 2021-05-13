import math

a,b,c,d = map(int, input().split())

lcm = int(c*d / math.gcd(c,d))

def num(i):
  ans = b//i - a//i
  if a % i == 0:
    ans +=1
  return ans

lcm_num = num(lcm)

cd_num  = num(c) + num(d)

num = cd_num - lcm_num

print(b-a+1-num)