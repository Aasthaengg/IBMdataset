N = int(input())
min = 100000000000000
for i in range(1, N):
  A = str(i)
  B = str(N - i)
  ref = 0
  for a in A:
    ref += int(a)
  for b in B:
    ref += int(b)
  if ref < min:
    min = ref
print(min)