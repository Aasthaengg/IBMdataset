X, Y = list(map(int,input().split()))

for i in range(X + 1):
   for j in range(X + 1):
      if 2 * i + 4 * j == Y and i + j == X:
         print('Yes')
         exit()

print('No')