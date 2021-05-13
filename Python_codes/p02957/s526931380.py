# 2020/04/25
# AtCoder Beginner Contest 135- A

# Input
a, b = map(int,input().split())

# Calc
ans = int((a + b) / 2)
if ans != (a + b) / 2:
    ans = 'IMPOSSIBLE'

# Output
print(ans)
