n = int(input())
a = list(map(int, input().split()))
gray = 399
brown = 799
green = 1199
lblue = 1599
blue = 1999
yellow = 2399
orange = 2799
red = 3199
count = 0
result = [0, 0, 0, 0, 0, 0, 0, 0]
for i in a:
    if 0 < i <= gray:
        result[0] += 1
    elif gray < i <= brown:
        result[1] += 1
    elif brown < i <= green:
        result[2] += 1
    elif green < i <= lblue:
        result[3] += 1
    elif lblue < i <= blue:
        result[4] += 1
    elif blue < i <= yellow:
        result[5] += 1
    elif yellow < i <= orange:
        result[6] += 1
    elif orange < i <= red:
        result[7] += 1
    else:
        count += 1
minout = sum(i>0 for i in result)
maxout = minout + count
if minout == 0:
    minout = 1
print(minout, maxout)
