s=input()
w=int(input())
import math
n = math.ceil(len(s) / w)
ans=""
for i in range(n):
  ans += s[i * w]
print(ans)