A = list(input().split())
for i in range(2):
  if A[i][-1] != A[i + 1][0]:
    print('NO')
    exit()
print('YES')