# 2020/07/23
# AtCoder Beginner Contest 154 - A

# Input
s, t = input().split()
a, b = map(int,input().split())
u = input()

aa = a
ab = b

# Calc
if s == u:
    aa = aa - 1
elif t == u:
    ab = ab - 1

# Output
print(aa, ab)
