# 2019/05/12
# AtCoder Beginner Contest 098 - A

# Input
a, b = map(int, input().split())

# Calc
c_max = a + b
mi = a - b
ti = a * b

if c_max < mi:
    c_max = mi
if c_max < ti:
    c_max = ti
    
# Output
print(c_max)
