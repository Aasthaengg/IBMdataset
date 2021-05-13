import math
A, B = map(int, input().split())
A_min = A / 0.08
A_max = (A + 1) / 0.08
B_min = B / 0.1
B_max = (B + 1) / 0.1

for i in range(1, 1001):
  if int(i * 0.08) == A and int(i * 0.1) == B:
    print(i)
    exit()
print(-1)