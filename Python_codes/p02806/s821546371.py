import numpy as np
n = int(input())

s = [''] * n
time = [0] * n
for i in range(n):
    s[i], t = input().split()
    time[i:] = [j + int(t) for j in time[i:]]
x = input()
index = 0
while True:
    if s[index] == x:
        break
    index += 1
print(time[n-1]-time[index])
