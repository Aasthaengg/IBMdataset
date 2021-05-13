import math
s = input()
ans = int(math.floor(len(s) / 2) - s.count('p'))
print(ans)