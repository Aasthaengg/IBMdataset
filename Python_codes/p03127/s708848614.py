n = int(input())
A = list(map(int, input().split()))
A.sort()
while len(A) > 1:
  a = [A[0]]
  for i in range(1, len(A)):
    if A[i]%A[0] == 0: continue
    else: a.append(A[i]%A[0])
  A = sorted(a)
print(A[0])