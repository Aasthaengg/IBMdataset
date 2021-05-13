import sys
A, B, C = map(int, input().split())

for i in range(100):
  if C == (A*i%B):
    print("YES")
    sys.exit()
print("NO")
