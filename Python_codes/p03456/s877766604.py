# 2020/08/10
# AtCoder Beginner Contest 086 - B

# Input
a, b = input().split()
ab = int(a + b)

# Calc
if ab ** (1/2) - int(ab ** (1/2)) == 0:
    ans = 'Yes'
else:
    ans = 'No'

# Output
print(ans)
