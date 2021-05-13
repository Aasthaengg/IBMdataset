import sys

s = sys.stdin.readline().strip()

n = len(s)
p_n = s.count("p")
ans = n // 2 - p_n
print(ans)