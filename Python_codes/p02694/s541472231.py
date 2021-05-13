import math
x = int(input())

an = 100
cnt = 0

while(an < x):
    an += an//100
    cnt += 1

print(cnt)