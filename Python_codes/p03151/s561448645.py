from bisect import bisect_left
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = [0]*N

for i in range(N):
  C[i] = A[i] - B[i]
C.sort()
if sum(C) < 0:
  ans = -1
else:
  b = bisect_left(C,0)
  C_minus = C[:b]
  sum_C_minus = sum(C_minus)
  if sum_C_minus == 0:
    ans = 0
  else:
    count = len(C_minus)
    C_plus = C[b:]
    C_plus.sort(reverse = True)
    for j in range(len(C_plus)):
      count += 1
      if abs(sum_C_minus) <= C_plus[j]:
        ans = count
        break
      else: sum_C_minus += C_plus[j]

print(ans)