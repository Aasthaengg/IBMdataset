import sys
N = int(input())
array = list(map(int,input().split()))

if not ( 1 <= N <= 100 ): sys.exit()
if (min(array) < 1) or (max(array) > 1000) : sys.exit()

sum = 0
for J in array:
    sum += 1/J

print(1/sum)