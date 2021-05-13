import sys
readline = sys.stdin.readline

ans = ""
for i in range(3):
  ans += readline().strip()[i]
  
print(ans)