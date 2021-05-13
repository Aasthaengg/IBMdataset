import sys
n, y = map(int, input().split())

max10k = y // 10000

for i in range(max10k+1):
    max5k = (y - 10000 * i)//5000
    for j in range(max5k+1):
        if (y - 10000 * i - 5000 * j) // 1000 == n - i - j:
          print(i, j, (n - i - j))
          sys.exit()

print(-1,-1,-1)
