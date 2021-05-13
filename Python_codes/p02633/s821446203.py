import sys
input = sys.stdin.readline


x = int(input())

k = 0
for i in range(1,10000):
    if x*i%360 == 0:
        k = i
        break
print(k)