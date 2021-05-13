import math

num = input()

l = len(num)

k = 0
for i in range(l):
    k += int(num[i])

ans = k % 9

if ans == 0:
    print("Yes")

else:
    print("No")