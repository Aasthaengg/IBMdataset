# coding: utf-8
# Your code here!
k, s = map(int, input().rstrip().split())
result = 0
for x in range(k+1):
    if 2*k >= s - x:
        for y in range(k+1):
            if s - x - y >= 0 and s - x - y <= k:
                result += 1

print(result)