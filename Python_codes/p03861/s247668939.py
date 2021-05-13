import math
a, b, x = map(int, input().split())
bwaru = b//x
awaru = (a-1)//x
ans = bwaru-awaru
print(ans)
