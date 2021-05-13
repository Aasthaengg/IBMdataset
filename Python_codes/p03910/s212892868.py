import math
n = int(input())

li = [False] * (n + 1)

s = 0
for i in range(1, n+1):
    s += i
    li[i] = True

    if s == n:
        break
    if n - s < i + 1:
        li[i+1-(n-s)] = False
        s -= i+1-(n-s)

# print(li)
for j in range(1, i+1):
    if li[j]:
        print(j)
