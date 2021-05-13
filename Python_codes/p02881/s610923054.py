import math
n = int(input())

rn = int(math.sqrt(n))

ans_l = []
for i in range(1, rn+1):
  if n%i == 0:
    ans_l.append(i+n//i-2)

print(min(ans_l))