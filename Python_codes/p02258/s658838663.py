import sys
n = int(input())
r = [int(input()) for x in range(n)]
max_val = sys.maxsize * -1
min_val = r[0]
for i in range(1,n):
  max_val = max(max_val, r[i] - min_val)
  min_val = min(min_val, r[i])
print(max_val)

