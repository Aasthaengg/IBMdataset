import math

x = int(input())
ans = (x // 11) * 2
ans += math.ceil((x%11) / 6)
print(ans)
