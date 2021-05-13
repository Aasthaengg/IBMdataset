x, y = map(int, input().split())

# kame = x - turu
# 2*turu + 4*kame = y
# 2*turu + 4*(x - turu) = y
#  -2*turu + 4x - y = 0
# turu = 2x - 1/2*y

turu = 2*x - 1/2*y
if(turu.is_integer() and turu >= 0 and (x-turu) >= 0):
    print("Yes")
else:
    print("No")
