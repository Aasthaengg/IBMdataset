import sys
readline = sys.stdin.readline

S = readline().rstrip()

ans = 10 ** 10
for i in range(ord("a"),ord("z") + 1):
  ans = min(ans, max(map(len,S.split(chr(i)))))
  
print(ans)
