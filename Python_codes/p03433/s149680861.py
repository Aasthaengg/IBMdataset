N, A = int(input()), int(input())
for i in range(A + 1):
  if (N - i) % 500 == 0:
    print('Yes')
    exit()
print('No')
