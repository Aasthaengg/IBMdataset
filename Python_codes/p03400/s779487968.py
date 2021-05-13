import math
n = int(input())
d,x = map(int, input().split())
lis = []
for i in range(n):
    lis.append(int(input()))
    
cnt = 0
for i in lis:
    cnt += math.ceil(d/i)

print(cnt+x)