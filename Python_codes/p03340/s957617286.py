import math
n = int(input())
a = [int(x) for x in input().split()]

bit = int(math.log2(max(a+[1])))+1
key = [0]*bit
ans = 0
ans_bef = 0
for i in range(n):
  value = a[i]
  max_len = ans_bef
  for j in range(bit):
    if value%2 == 1:
      if max_len > key[j]:
        max_len = key[j]
      key[j] = 0
    else:
      key[j] += 1
    value //= 2
  ans_bef = max_len+1
  ans += max_len
      
ans += n
print(ans)