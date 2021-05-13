# 8 = 2 * 2 * 2
# 6 = 2 * 3
x,y= map(int,(input().split()))

result = 0

if x % y == 0:
    result = -1
else:
    result = x 


print(result)
