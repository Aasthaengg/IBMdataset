N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for Z in range(X+1, Y+1):
  if all([i < Z for i in x]) and all([i >= Z for i in y]):
    print('No War')
    exit()

print('War')