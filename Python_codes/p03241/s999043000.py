import math
N, M = [int(i) for i in input().split()]
# for i in range(min(math.floor(math.sqrt(M)), M//N), 0, -1):
#   if M % i == 0:
#     if M // i <= M//N:
#       print(max(i, M // i))
#     else:
#       print(i)
#     break

ans = 1
for i in range(1, math.floor(M**0.5)+1):
  if M % i == 0:
    if M//i <= M//N:
      ans = max(ans, M//i)
    elif i <= M//N:
      ans = max(ans, i)
print(ans)

