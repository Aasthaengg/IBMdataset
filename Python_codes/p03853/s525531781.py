import numpy as np

s = input().split()

# 縦の長さ
h = int(s[0])

# 横の長さ
w = int(s[1])


answer = []

for num in range(h):
    x = input().split()
    answer.append(x[0])
    answer.append(x[0])

for num in range(h * 2):
    print(answer[num])




