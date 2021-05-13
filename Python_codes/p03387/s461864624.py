# 2020/07/18
# AtCoder Beginner Contest 093 - C

# Input
abc = list(map(int,input().split()))
abc.sort()

ans = 0

s1 = abc[2] - abc[0]
s2 = abc[2] - abc[1]

# Calc
if s1 > 0:
    # even & even
    if s1 % 2 == 0 and s2 % 2 == 0:
        ans = s1 // 2 + s2 // 2
        
    # odd & odd
    elif s1 % 2 > 0 and s2 % 2 > 0:
        s1 = s1 - 1
        s2 = s2 - 1
        ans = s1 // 2 + s2 // 2 + 1
    # odd & even(eg:5 2 3)
    else:
        ans = s1 // 2 + s2 // 2 + 2

# Output
print(ans)
