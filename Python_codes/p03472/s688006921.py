import math


N,H = map(int, input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

nage_count = 0
huri_count = 0
A_max = max(A)
for b in sorted(B, reverse = True):
  if b > A_max:
    nage_count += 1
    H -= b
    if H <= 0:
      break
  else: 
    break

# 今度は一番強いやつを振り続ける. 
if H>0:
  huri_count = math.ceil(H/A_max)
print(huri_count + nage_count)