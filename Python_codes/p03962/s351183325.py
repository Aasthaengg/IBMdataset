A = sorted(list(map(int, input().split())))
cnt = 1
for i in range(1, len(A)):
  if A[i] != A[i - 1]:
    cnt += 1
print(cnt)