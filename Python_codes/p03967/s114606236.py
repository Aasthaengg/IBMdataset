import sys
input = sys.stdin.readline
s = list(input())[: -1]
res = 0
g = s.count("g")
p = s.count("p")
print((g + p) // 2 - p)