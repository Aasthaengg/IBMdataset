import sys
readline = sys.stdin.readline

K = int(readline())

A = "ACL"
ans = ""
while K:
  if K & 1:
    ans += A
  A *= 2
  K >>= 1

print(ans)