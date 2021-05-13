N, H = map(int, input().split())
A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
A.sort(reverse = True)
B.sort(reverse = True)
count = 0
for b in B:
  if b > A[0]:
    H -= b
    count += 1
  else:
    break
  if H <= 0:
    break
if H > 0:
  count += (H + A[0] - 1) // A[0]
print(count)