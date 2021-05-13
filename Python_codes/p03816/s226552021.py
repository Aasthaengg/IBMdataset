from collections import Counter

n = int(input())
m = sum(v - 1 for v in Counter([int(i) for i in input().split()]).values())
print(n - round(m + 0.5))