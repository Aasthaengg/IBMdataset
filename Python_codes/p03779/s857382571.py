# 2020/06/09
# AtCoder Beginner Contest 056 - C

# Input
x = int(input())

wkx = 0
idx = 0

while wkx < x:
    idx = idx + 1
    wkx = wkx + idx

# Output
print(idx)
