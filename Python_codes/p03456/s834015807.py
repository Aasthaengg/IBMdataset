import math
a, b = input().split()
S = a+b
S = int(S)
S = math.sqrt(S)
if S.is_integer():
    ans = "Yes"
else:
    ans = "No"
print(ans)
