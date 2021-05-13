# 2019/05/12
# AtCoder Beginner Contest 098 - A

# Input
a, b = map(int, input().split())

# Calc
c_max = max(a+b, a-b, a*b)

# Output
print(c_max)
