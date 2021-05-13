x = int(input())
import math
ans = 0
ans = (x // 11)*2
ans += math.ceil((x%11)/6)
print (ans)