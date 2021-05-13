import math

a, b, x = map(int, input().split())

if x/(a*a*b) <= 0.5: #水が水筒の半分以下の場合
    area = x/a
    tan = area*2/(b*b)
    d = 90 - math.degrees(math.atan(tan))
else:
    rest = (a*a*b - x)/a
    tan = rest*2/(a*a) #空の部分の面積は、a*atanθ/2 = a*a*b - x
    d = math.degrees(math.atan(tan))

print(d)