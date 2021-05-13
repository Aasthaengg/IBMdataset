# 2020/05/22
# AtCoder Beginner Contest 072 - D

# Input
n = int(input())
p = list(map(int,input().split()))

i = 0
cnt = 0
while i < n:
    if p[i] == i+1:
        cnt = cnt + 1
        i = i + 2
    else:
        i = i + 1

# Output
print(cnt)
